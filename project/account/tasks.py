from .models import Emails
from celery import shared_task


@shared_task
def sendEmail(email, content):
    try:
        Emails.objects.create(email=email, content=content)
        return 'Email    created successfully'
    except Exception as e:
        # Log the error or handle it accordingly
        return f'Error creating email: {e}'