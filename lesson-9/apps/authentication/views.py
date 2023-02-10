from django.contrib.auth import get_user_model, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView, TemplateView, View

from apps.authentication.forms import LoginForm, RegistrationForm

User = get_user_model()


class LoginView(FormView):
    form_class = LoginForm
    template_name = 'authentication/login.html'
    success_url = reverse_lazy('auth:account')

    def form_valid(self, form):
        login(self.request, User.objects.get(email=form.cleaned_data['email']))
        return super().form_valid(form)


class RegisterView(CreateView):
    form_class = RegistrationForm
    template_name = 'authentication/register.html'
    success_url = reverse_lazy('auth:login')


class AccountView(LoginRequiredMixin, TemplateView):
    template_name = 'authentication/account.html'


class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/auth/login')
