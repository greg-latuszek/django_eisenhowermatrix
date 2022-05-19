from celery import shared_task

from django.core.mail import EmailMessage


@shared_task(ignore_result=True)
def do_send_mail(subject, body, from_email, to_email):
    email_message = EmailMessage(
        subject=subject, body=body, from_email=from_email, to=[to_email]
    )
    email_message.send()
