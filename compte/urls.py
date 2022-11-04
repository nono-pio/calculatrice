from django.urls import path

from compte.views import *

urlpatterns = [
    path('', compte_view, name = 'compte'),
    path('login/', login_view, name= 'login'),
    path('logout', logout_view, name='logout'),
    path('register/', register_view, name= 'register')
]