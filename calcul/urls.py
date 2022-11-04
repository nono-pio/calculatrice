from django.urls import path
from calcul.views import *

urlpatterns = [
    path('', calcul_view, name = 'calcul')
]