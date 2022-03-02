
from django.conf import settings
from django.core.mail import send_mail
def seend_order_message(order_sn):
    subject = 'GreaterWMS开源硬件商城'
    email = settings.PUBLIC_EMAIL
    message = '客户订单邮件'
    recipient_list = [email, ]
    html_message = "<h1>工作人员您好，您的硬件商城有新的订单生成,订单号为：%s，请去硬件商城的后台进行查看，并安排发货。<br/>" % (order_sn)
    result = send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list, html_message=html_message)
    if result == 1:
        return True  # 短信发送成功
    else:
        return False



# if __name__ == '__main__':
#     res=seend_order_message(111111)
#     print(res)