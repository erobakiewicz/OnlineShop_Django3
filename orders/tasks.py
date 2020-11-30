# Celery tasks
from celery import task
from OnlineShop_Django3.celery_settings import app
from django.core.mail import send_mail
from .models import Order


@task
def order_created(order_id):
    """
    Task to send an email notification when an order is placed.
    :param order_id:
    :return:
    """
    print('start')
    order = Order.objects.get(id=order_id)
    subject = f'Order nr. {order.id}'
    message = f'Dear {order.first_name},\n\n' \
              f'You have successfully placed an order.' \
              f'Your order ID is {order.id}.'
    mail_sent = send_mail(subject,
                          message,
                          'admin@myshop.com',
                          [order.email])
    print('finish')
    return mail_sent