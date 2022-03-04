
from VueDjangoFrameWorkShop.settings import PUBLIC_EMAIL,EMAIL_HOST_USER
from django.core.mail import send_mail
def seend_order_message(order_sn,mode):
    subject = 'GreaterWMS开源硬件商城'
    email = PUBLIC_EMAIL
    message = '客户订单邮件'
    recipient_list = [email, ]
    if mode == 1:
        html_message = "<h1>工作人员您好，您的硬件商城有<新的订单生成>,订单号为：%s，请去硬件商城的后台进行查看，并安排发货。<br/>" % (order_sn)
    else:
        html_message = "<h1>工作人员您好，您的硬件商城有<订单被用户取消>,订单号为：%s，请去硬件商城的后台进行查看<br/>" % (order_sn)
    result = send_mail(subject, message,EMAIL_HOST_USER, recipient_list, html_message=html_message)
    if result == 1:
        return True  # 短信发送成功
    else:
        return False



# if __name__ == '__main__':
#     res=seend_order_message(111111)
#     print(res)