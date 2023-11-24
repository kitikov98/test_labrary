from celery import shared_task
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags


@shared_task
def send_welcome_email(user_email):
    subject = 'Добро пожаловать к нам!'
    message = render_to_string('welcome_email_template.html', {'user_email': user_email})
    plain_message = strip_tags(message)
    from_email = 'ipavlovich007@yandex.by'
    to_email = [user_email]
    send_mail(subject, plain_message, from_email, to_email, html_message=message)
