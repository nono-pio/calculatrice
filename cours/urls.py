from django.urls import path

from cours.views import *

urlpatterns = [
    path('', cours_view, name = 'cours'),
]