from django.urls import path

from apps.authentication.views import login_view, acc_view, logout_view

app_name = 'authentication'

urlpatterns = [
    path('login/', login_view),
    path('logout/', logout_view),
    path('account/', acc_view)
]
