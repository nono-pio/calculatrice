from django.urls import path
from fonction.views import *

urlpatterns = [
    path('', fonction_view, name = 'fonction')
]
