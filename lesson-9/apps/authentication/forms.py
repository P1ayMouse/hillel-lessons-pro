from django import forms
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.mail import EmailMultiAlternatives
from django.utils.translation import gettext_lazy as _
from apps.authentication.models import UserToken

User = get_user_model()


class LoginForm(forms.Form):
    email = forms.EmailField(label=_('Email Adress'))
    password = forms.CharField(label=_('Password'), widget=forms.PasswordInput)

    def clean(self):
        user = User.objects.filter(email=self.cleaned_data['email']).first()

        if user is None:
            raise forms.ValidationError("Unknown user or password")

        if not user.check_password(self.cleaned_data['password']):
            raise forms.ValidationError("Unknown user or password")


def send_email_confirm(user):
    token = UserToken.objects.create(user=user)

    email = EmailMultiAlternatives(
        "Confirm your email address.",
        f"Please confirm your email by visiting {settings.SITE_URL}/auth/confirm/{token.token}/",
        settings.DEFAULT_FROM_EMAIL,
        [user.email]
    )

    email.attach_alternative(f'<h1> Please confirm your email </h1><br/> '
                             f'<a href="{settings.SITE_URL}/auth/confirm/{token.token}">visit link</a>', 'text/html')

    email.send()


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password']
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    def clean_password2(self):
        password = self.cleaned_data['password']
        password2 = self.cleaned_data['password2']
        if password2 != password:
            raise forms.ValidationError('Password mismatch')
        return password2

    def save(self, commit=True):
        user = super().save(commit)
        if commit:
            user.set_password(self.cleaned_data['password'])
            user.is_active = False
            user.save()
            send_email_confirm(user)
        return user
