from celery import shared_task

from django.core.mail import EmailMessage


@shared_task(ignore_result=True)
def do_send_mail(subject, body, from_email, to_email):
    email_message = EmailMessage(subject=subject, body=body, from_email=from_email, to=[to_email])
    print(f">>>>>>>>>>>>>>>>>--[><]-->>>> Sending mail(from: {from_email}, to: {to_email}, subject: {subject}")
    email_message.send()
    print(f">>>>>>>>>>>>>>>>>>>>>>>--[><] Sent    mail(from: {from_email}, to: {to_email}, subject: {subject}")
