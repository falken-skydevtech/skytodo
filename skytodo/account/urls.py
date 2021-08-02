from django.urls import path, include
from .views.user import login, logout, register, start

urlpatterns = [
    path('account/login', login, name='account-login'),
    path('account/register', register, name='account-register'),
    path('account/logout', logout, name='account-logout'),
]
