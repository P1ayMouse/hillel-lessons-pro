from django.contrib.auth import get_user_model, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render


User = get_user_model()


def login_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/auth/account')
    if request.method == 'POST':
        user = User.objects.get(email=request.POST['email'])

        if user.check_password(request.POST['password']):
            login(request, user)
            return HttpResponseRedirect(request.GET.get('next', '/'))

    return HttpResponse(render(request, 'authentication/login.html'))


@login_required
def acc_view(request):
    return HttpResponse(render(request, 'authentication/account.html'))


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('auth/login/')
