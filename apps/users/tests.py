from django.test import TestCase

# Create your tests here.

from qcloudsms_py import SmsSingleSender
from qcloudsms_py.httpclient import HTTPError
# def send_sms(moible,code):
#     ssender = SmsSingleSender(1400576604,"a83ab9b471c3538ab3a07550b4d00117")
#     params=[code,]
#     try:
#         result = ssender.send_with_param(86, moible,1138960, params, "读书空间站", extend="", ext="")
#         # print(result)
#     except Exception as e:
#         print('手机号为：(%s)短信发送失败：%s'%(moible,str(e)))
#
#     if result.get('result')==0:
#           return True
#     else:
#         print('手机号为：(%s)短信发送异常：%s' %(moible,result['errmsg']))
#     return False
#
# if __name__ == '__main__':
#     res=send_sms('15203664920',1234)
#     # print(res)



import requests

# POST / HTTP/1.1
# Host: sms.tencentcloudapi.com
# Content-Type: application/json
# X-TC-Action: SendSms
# <公共请求参数>

# data={
#     "Action":"SendSms",
#     "Version":"2021-01-11",
#     "Region":"上海",
#     "PhoneNumberSet": [
#         "+8615203664920",
#     ],
#     "SmsSdkAppId": "1400576604",
#     "SignName": "腾讯云",
#     "TemplateId": "1138960",
#     "TemplateParamSet": [
#         "12345"
#     ],
#     "SessionContext": "test"
# }
# headers = {
# 'Content-Type': 'application/json',
# 'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.76 Mobile Safari/537.36',
# }
# r=requests.post("http://sms.tencentcloudapi.com",data=data)
# print(r)


import ssl


from qcloudsms_py import SmsMultiSender, SmsSingleSender
from qcloudsms_py.httpclient import HTTPError
from django.conf import settings

def send_sms_single(phone_num, template_param_list):
    """
    单条发送短信
    :param phone_num: 手机号
    :param template_id: 腾讯云短信模板ID
    :param template_param_list: 短信模板所需参数列表，例如:【验证码：{1}，描述：{2}】，则传递参数 [888,666]按顺序去格式化模板
    :return:
    """

    APPID = 1400576604
    APPKEY = "a83ab9b471c3538ab3a07550b4d00117"
    TEMPLATE_ID = 1138960
    SMS_SIGN = "读书空间站"

    # appid = settings.TENCENT_SMS_APP_ID  # 自己应用ID
    # appkey = settings.TENCENT_SMS_APP_KEY  # 自己应用Key
    # sms_sign = settings.TENCENT_SMS_SIGN  # 自己腾讯云创建签名时填写的签名内容（使用公众号的话这个值一般是公众号全称或简称）
    sender = SmsSingleSender(APPID, APPKEY)
    try:
        response = sender.send_with_param(86, phone_num,TEMPLATE_ID, template_param_list, sign=SMS_SIGN)
    except HTTPError as e:
        response = {'result': 1000, 'errmsg': "网络异常发送失败"}
    return response


if __name__ == '__main__':
    res=send_sms_single('',[1111,])
    print(res)



