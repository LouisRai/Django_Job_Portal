from .base import *
from django.contrib.messages import constants as messages

SECRET_KEY = 'django-insecure-oti6f7izv(nv+^hrt#$qo6j_q)9+@$uk1g6+7k=zz^sg7f1wo7'

DEBUG = True

ALLOWED_HOSTS = ["*"]

EMAIL_HOST = 'sandbox.smtp.mailtrap.io'
EMAIL_HOST_USER = 'a68b0514a96fc9'
EMAIL_HOST_PASSWORD = '942a6f5a1c1cf4'
EMAIL_PORT = '2525'

MESSAGE_TAGS = {
messages.DEBUG: 'alert-info',
messages.INFO: 'alert-info',
messages.SUCCESS: 'alert-success',
messages.WARNING: 'alert-warning',
messages.ERROR: 'alert-danger',
}