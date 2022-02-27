from django.views.generic.base import RedirectView, View
from rest_framework.mixins import CreateModelMixin
from random import choice

from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.shortcuts import render
# 但是当第三方模块根本不知道你的user model在哪里如何导入呢
from django.contrib.auth import get_user_model
# 这个方法会去setting中找AUTH_USER_MODEL
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework_jwt.serializers import jwt_payload_handler, jwt_encode_handler

from VueDjangoFrameWorkShop.settings import APIKEY
from rest_framework.response import Response
from rest_framework import mixins, permissions, authentication
from rest_framework import viewsets, status
from users.models import VerifyCode
from users.serializers import SmsSerializer, UserRegSerializer, UserDetailSerializer,SmsModelSerializer,UserCodeLoginModelSerializer
from utils.yunpian import YunPian,SmsCode
from rest_framework.exceptions import APIException
from datetime import datetime, timedelta
User = get_user_model()


# 发送验证码是创建model中一条记录的操作
# Create your views here.


class CustomBackend(ModelBackend):
    """
    自定义用户验证规则
    """

    def authenticate(self, username=None, password=None, **kwargs):
        try:
            # 不希望用户存在两个，get只能有一个。两个是get失败的一种原因
            # 后期可以添加邮箱验证
            user = User.objects.get(
                Q(username=username) | Q(mobile=username))
            # django的后台中密码加密：所以不能password==password
            # UserProfile继承的AbstractUser中有def check_password(self,
            # raw_password):
            if user.check_password(password):
                return user
        except Exception as e:
            return None
from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet
class MobileView(ViewSet):

    @action(methods=['GET'], detail=False)
    def mobile(self, request):
        username = request.query_params.get('username')
        try:
            User.objects.get(mobile=username)
            return Response(data={'code':200,'details':'手机号存在'})
        except Exception:
            return Response(data={'code':404,'details':'手机号不存在'})
import re
from VueDjangoFrameWorkShop.settings import REGEX_MOBILE
class SmsSendCodeView(CreateModelMixin,viewsets.GenericViewSet):
    authentication_classes = ()
    serializer_class = SmsModelSerializer

    def generate_code(self):
        """
        生成四位数字的验证码字符串
        """
        seeds = "1234567890"
        random_str = []
        for i in range(4):
            random_str.append(choice(seeds))

        return "".join(random_str)

    def create(self, request, *args, **kwargs):
        # 验证手机号码是否合法
        username = self.request.data.get('username')
        if not re.match(REGEX_MOBILE, username):
            raise APIException({"detail": "手机格式不合法"})

        # 手机是否注册
        if not User.objects.filter(mobile=username).exists():
            raise APIException({"detail": "用户名错误"})
        # 验证码发送频率
        one_mintes_ago = datetime.now() - timedelta(hours=0, minutes=1, seconds=0)
        # 添加时间大于一分钟以前。也就是距离现在还不足一分钟
        if VerifyCode.objects.filter(add_time__gt=one_mintes_ago, mobile=username).count():
            raise APIException({"detail": "距离上一次发送未超过60s"})
        code = self.generate_code()
        res = SmsCode()
        sms_status = res.send(username,'1316599',code)  # 登录验证码
        print(sms_status)
        if sms_status != 'Ok':
            return Response({
                "detail": '短信发送失败'
            }, status=status.HTTP_400_BAD_REQUEST)
        else:
            code_record = VerifyCode(code=code, mobile=username)
            code_record.save()
            return Response({
                "detail": '短信发送成功','username':username
            }, status=status.HTTP_201_CREATED)


class CodeLoginViewSet(CreateModelMixin,viewsets.GenericViewSet):
    '''
    验证码登录
    '''
    authentication_classes = ()
    serializer_class = UserCodeLoginModelSerializer
    queryset = User.objects.all()

    def create(self, request, *args, **kwargs):
        username = self.request.data.get('username')
        if not re.match(REGEX_MOBILE, username):
            raise APIException({"detail": "手机格式不合法"})
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        token = serializer.context.get('token')
        username = serializer.context.get('username')
        headers = self.get_success_headers(serializer.data)
        return Response(data={'token':token,'username':username}, status=status.HTTP_201_CREATED, headers=headers)


class SmsCodeViewset(CreateModelMixin, viewsets.GenericViewSet):
    """
    发送短信验证码
    """
    authentication_classes = ()
    serializer_class = SmsSerializer

    def generate_code(self):
        """
        生成四位数字的验证码字符串
        """
        seeds = "1234567890"
        random_str = []
        for i in range(4):
            random_str.append(choice(seeds))

        return "".join(random_str)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        mobile = serializer.validated_data["mobile"]

        # yun_pian = YunPian(APIKEY)

        code = self.generate_code()
        # sms_status=send_sms(mobile,code)
        # tencent_send=Tencent()
        # sms_status=tencent_send.send_sms(mobile,code)
        res = SmsCode()
        sms_status = res.send(mobile,"1314402", code) # 注册验证码
        print(sms_status)
        if sms_status != 'Ok':
            return Response({
                "mobile": '短信发送失败'
            }, status=status.HTTP_400_BAD_REQUEST)
        else:
            code_record = VerifyCode(code=code, mobile=mobile)
            code_record.save()
            return Response({
                "mobile": mobile
            }, status=status.HTTP_201_CREATED)


class UserViewset(CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    用户
    """
    authentication_classes = ()
    serializer_class = UserRegSerializer
    queryset = User.objects.all()

    # authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication)

    def get_serializer_class(self):
        if self.action == "retrieve":
            return UserDetailSerializer
        elif self.action == "create":
            return UserRegSerializer

        return UserDetailSerializer

    # permission_classes = (permissions.IsAuthenticated, )
    def get_permissions(self):
        if self.action == "retrieve":
            # return [permissions.IsAuthenticated()]
            return []
        elif self.action == "create":
            return []

        return []

    def create(self, request, *args, **kwargs):
        authentication_classes = ()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)

        re_dict = serializer.data
        payload = jwt_payload_handler(user)
        re_dict["token"] = jwt_encode_handler(payload)
        re_dict["name"] = user.name if user.name else user.username

        headers = self.get_success_headers(serializer.data)
        return Response(re_dict, status=status.HTTP_201_CREATED, headers=headers)

    # 重写该方法，不管传什么id，都只返回当前用户
    def get_object(self):
        return self.request.user

    def perform_create(self, serializer):
        return serializer.save()


class IndexView(View):
    # 直接调用get方法免去判断
    def get(self, request):
        # render就是渲染html返回用户
        # render三变量: request 模板名称 一个字典写明传给前端的值
        return render(request, "index.html")


favicon_view = RedirectView.as_view(
    url='http://vueshopstatic.mtianyan.cn/daishu/favicon.ico', permanent=True)
