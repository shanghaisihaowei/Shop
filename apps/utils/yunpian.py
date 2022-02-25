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


from qcloudsms_py import SmsSingleSender

def send_sms(mobile,code):
    # ssender = SmsSingleSender(1400576604, 'a83ab9b471c3538ab3a07550b4d00117')
    ssender = SmsSingleSender(1400637827, '32fab9e0fc54e3c70b1e3e82a5a6e788')
    params = [code, ]
    try:
        result = ssender.send_with_param(86, mobile,
          1314402, params, sign="四号位信息科技有限公司", extend="", ext="")
    except Exception as e:
        print('手机号{}，发送短信失败，错误原因是{}'.format(mobile, str(e)))
        return False
    if result['result'] != 0:
        print('手机号{}，发送短信失败，错误原因是{}'.format(mobile, result['errmsg']))
        return False
    return True



