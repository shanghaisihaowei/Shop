from datetime import datetime

from django.shortcuts import render, redirect

# Create your views here.
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from rest_framework import viewsets, mixins
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from trade.models import ShoppingCart, OrderInfo, OrderGoods
from trade.serializers import ShopCartSerializer, ShopCartDetailSerializer, OrderSerializer, OrderDetailSerializer
from utils.permissions import IsOwnerOrReadOnly
from goods.models import Goods
from utils.send_email import seend_order_message
class ShoppingCartViewset(viewsets.ModelViewSet):
    """
    购物车功能
    list:
        获取购物车详情
    create：
        加入购物车
    delete：
        删除购物记录
    """
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    serializer_class = ShopCartSerializer
    lookup_field = "goods_id"

    # 库存数-1
    def perform_create(self, serializer):
        shop_cart = serializer.save()
        goods = shop_cart.goods
        goods.goods_num -= shop_cart.nums
        goods.save()

    # 库存数+1
    def perform_destroy(self, instance):
        print(self.request.data)
        goods = instance.goods
        goods.goods_num += instance.nums
        goods.save()
        # 取goods在del之前取之后就被删掉了
        instance.delete()

    # 更新库存
    def perform_update(self, serializer):
        existed_record = ShoppingCart.objects.get(id=serializer.instance.id)
        existed_nums = existed_record.nums
        # 先保存之前的数据existed_nums
        saved_record = serializer.save()
        # 变化的数量
        nums = saved_record.nums - existed_nums
        goods = saved_record.goods
        goods.goods_num -= nums
        goods.save()

    def get_serializer_class(self):
        if self.action in ['list',]:
            return ShopCartDetailSerializer
        else:
            return ShopCartSerializer

    def get_queryset(self):
        return ShoppingCart.objects.filter(user=self.request.user)


from django.db.models import F
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
class DelShoppingCartView(ViewSet):
    """
    delete：
        删除购物记录
    """
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    def get_object(self):
        return self.request.user
    # def get_queryset(self):
    #     return ShoppingCart.objects.filter(user=self.request.user)
    @action(methods='DELETE', detail=False)
    def destroy(self, request):
        instance = self.get_object()
        print(instance)
        shop_carts = ShoppingCart.objects.filter(user=instance)
        print(shop_carts)
        for shop_cart in shop_carts:
            print(shop_cart.goods)
            goods_obj = Goods.objects.filter(id=shop_cart.goods.id).first()
            # goods_obj.goods = F('goods')+shop_cart.goods
            goods_obj.goods_num = F('goods_num')+shop_cart.nums
            goods_obj.save()

            shop_cart.delete()
        return Response(status=204)

from rest_framework import status

class OrderViewset(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin, mixins.DestroyModelMixin,
                   viewsets.GenericViewSet):
    """
    订单管理
    list:
        获取个人订单
    delete:
        删除订单
    create：
        新增订单
    """
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    serializer_class = OrderSerializer

    def get_queryset(self):
        return OrderInfo.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action == "retrieve":
            return OrderDetailSerializer
        return OrderSerializer

    def perform_create(self, serializer):
        order = serializer.save()
        # 获取到用户购物车里的商品
        shop_carts = ShoppingCart.objects.filter(user=self.request.user)
        for shop_cart in shop_carts:
            order_goods = OrderGoods()
            order_goods.goods = shop_cart.goods
            order_goods.goods_num = shop_cart.nums
            order_goods.order = order
            order_goods.save()

            shop_cart.delete()
        return order
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        Order_obj = OrderInfo.objects.filter(user=self.request.user.pk, order_sn=instance).first()
        if Order_obj:
            print(Order_obj.pay_status)
            if str(Order_obj.pay_status) == 'TRADE_SUCCESS':
                seend_order_message(instance, 0)
                self.perform_destroy(instance)
                return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                self.perform_destroy(instance)
                return Response(status=status.HTTP_204_NO_CONTENT)
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

from rest_framework.views import APIView
from utils.alipay import AliPay
from VueDjangoFrameWorkShop.settings import ali_pub_key_path, private_key_path,NOTIFY_URL,ALIPAY_APPID
from rest_framework.response import Response


class AlipayView(APIView):
    def get(self, request):
        """
        处理支付宝的return_url返回
        """
        processed_dict = {}
        # 1. 获取GET中参数
        for key, value in request.GET.items():
            processed_dict[key] = value
        # 2. 取出sign
        sign = processed_dict.pop("sign", None)

        # 3. 生成ALipay对象
        alipay = AliPay(
            appid=ALIPAY_APPID,
            # app_notify_url="http://47.98.167.5:8000/alipay/return/",
            app_notify_url=NOTIFY_URL,
            app_private_key_path=private_key_path,
            alipay_public_key_path=ali_pub_key_path,  # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
            debug=True,  # 默认False,
            return_url=NOTIFY_URL
            # return_url="http://47.98.167.5:8000/alipay/return/"
        )

        verify_re = alipay.verify(processed_dict, sign)

        # 这里可以不做操作。因为不管发不发return url。notify url都会修改订单状态。
        if verify_re is True:
            order_sn = processed_dict.get('out_trade_no', None)
            trade_no = processed_dict.get('trade_no', None)

            existed_orders = OrderInfo.objects.filter(order_sn=order_sn)
            for existed_order in existed_orders:
                existed_order.trade_no = trade_no
                existed_order.pay_time = datetime.now()
                existed_order.save()

            response = redirect("/index/#/app/home/member/order")

            # response.set_cookie("nextPath","pay", max_age=3)
            return response
        else:
            response = redirect("index")
            return response

    def post(self, request):
        """
        处理支付宝的notify_url
        """
        # 1. 先将sign剔除掉
        processed_dict = {}
        for key, value in request.POST.items():
            processed_dict[key] = value

        sign = processed_dict.pop("sign", None)

        # 2. 生成一个Alipay对象
        alipay = AliPay(
            appid=ALIPAY_APPID,
            # app_notify_url="http://47.98.167.5:8000/alipay/return/",
            app_notify_url=NOTIFY_URL,
            app_private_key_path=private_key_path,
            alipay_public_key_path=ali_pub_key_path,  # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
            # debug=True,  # 默认False,
            # return_url="http://47.98.167.5:8000/alipay/return/"
            return_url=NOTIFY_URL
        )

        # 3. 进行验签，确保这是支付宝给我们的
        verify_re = alipay.verify(processed_dict, sign)

        # 如果验签成功
        if verify_re is True:
            order_sn = processed_dict.get('out_trade_no', None)
            trade_no = processed_dict.get('trade_no', None)
            trade_status = processed_dict.get('trade_status', None)
            # 查询数据库中存在的订单
            existed_orders = OrderInfo.objects.filter(order_sn=order_sn)
            for existed_order in existed_orders:
                # 订单商品项
                order_goods = existed_order.goods.all()
                # 商品销量增加订单中数值
                for order_good in order_goods:
                    goods = order_good.goods
                    goods.sold_num += order_good.goods_num
                    goods.save()

                # 更新订单状态，填充支付宝给的交易凭证号。
                existed_order.pay_status = trade_status
                existed_order.trade_no = trade_no
                existed_order.pay_time = datetime.now()
                existed_order.save()
            order_str=order_sn
            seend_order_message(order_str,1)
            # 将success返回给支付宝，支付宝就不会一直不停的继续发消息了。
            return Response("success")
