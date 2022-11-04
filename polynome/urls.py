from django.urls import path
from polynome.views import *

urlpatterns = [
    path('', polynome_view, name = 'polynome'),
    path('returnpolynome/<str:polynome>', returnpolynome_view, name='returnpolynome')
]