from celery import shared_task
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.mail import EmailMultiAlternatives

from apps.authentication.models import UserToken

User = get_user_model()


@shared_task(autoretry_for=(Exception,),
             retry_kwargs={'max_retries': 5},
             default_retry_delay=30)
def send_email_confirmation(user_id):

    user = User.objects.get(id=user_id)

    token = UserToken.objects.create(user=user)

    email = EmailMultiAlternatives(
        "Confirm your email address.",
        f"Please confirm your email by visiting {settings.SITE_URL}/auth/confirm/{token.token}/",
        settings.DEFAULT_FROM_EMAIL,
        [user.email]
    )

    email.attach_alternative(f'<h1> Please confirm your email </h1><br/> '
                             f'<a href="{settings.SITE_URL}/auth/confirm/{token.token}">visit link</a>',
                             'text/html')

    email.send()


@shared_task
def remind_confirm_email():
    users = User.objects.filter(user_tokens__used_at=None, is_active=False)
    for user in users:
        print(user)
        send_email_confirmation.delay(user.id)
