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

data={
    "PhoneNumberSet": [
        "+8618511122266",
        "+8618511122233"
    ],
    "SmsSdkAppId": "1400006666",
    "SignName": "腾讯云",
    "TemplateId": "1234",
    "TemplateParamSet": [
        "12345"
    ],
    "SessionContext": "test"
}

r=requests.post("sms.tencentcloudapi.com",data=data)