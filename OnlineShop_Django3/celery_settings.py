import os
from celery import Celery

# set the default Django settings module for 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'OnlineShop_Django3.settings')

app = Celery('OnlineShop_Django3')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

