from django.urls import path
from .views import home, login_view, register, logout_view

urlpatterns = [
    path('', home, name = 'home'),
    path('accounts/login/', login_view, name= 'login'),
    path('accounts/register/', register, name='register'),
    path('accounts/logout/', logout_view, name= 'logout'),
]

