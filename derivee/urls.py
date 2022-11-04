from django.urls import path

from derivee.views import *

urlpatterns = [
    path('', derivee_view, name = 'derivee'),
    path('deriveereturn/', deriveeReturn_view, name= 'deriveereturn'),
]
