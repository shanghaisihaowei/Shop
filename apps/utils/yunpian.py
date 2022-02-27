# encoding: utf-8
__author__ = 'mtianyan'
__date__ = '2018/3/8 0008 09:28'
import json
import requests


class YunPian(object):

    def __init__(self, api_key):
        self.api_key = api_key
        self.single_send_url = "https://sms.yunpian.com/v2/sms/single_send.json"

    def send_sms(self, code, mobile):
        parmas = {
            "apikey": self.api_key,
            "mobile": mobile,
            "text": "【慕学生鲜】您的验证码是{code}。如非本人操作，请忽略本短信".format(code=code)
        }

        response = requests.post(self.single_send_url, data=parmas)
        re_dict = json.loads(response.text)
        return re_dict


# if __name__ == "__main__":
#     yun_pian = YunPian("")
#     yun_pian.send_sms("2017", "18092671458")


from tencentcloud.common import credential
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
# 导入 SMS 模块的client models
from tencentcloud.sms.v20190711 import sms_client, models
# 导入可选配置类
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile



class SmsCode:

  def __init__(self):
    self.cred = credential.Credential('AKID9k59wTjiQr2xby5vUmoa5JHzQaT5QUHo', "HH0SdXBXdRyEExPaU8VbQUHn1zg6F7j3")
    self.client = sms_client.SmsClient(self.cred, "ap-guangzhou")
    self.req = models.SendSmsRequest()
    self.req.SmsSdkAppid = '1400637827'
    self.req.Sign = "四号位信息科技有限公司"
    # self.req.TemplateID =  "1314402"
  def send(self, phone_number, sms_code):

    try:
      self.req.PhoneNumberSet = [f"+86{phone_number}".strip()]
      self.req.TemplateID = "1314402"
      self.req.TemplateParamSet = [sms_code]
      resp = self.client.SendSms(self.req)
      return resp.SendStatusSet[0].Code
    except TencentCloudSDKException as err:
      print(err)


if __name__ == '__main__':
    res=SmsCode()
    q=res.send('','1111')
    print(q)



