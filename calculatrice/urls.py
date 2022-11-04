from django.contrib import admin
from django.urls import path, include

from calculatrice.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name = 'home'),
    path('calcul/', include('calcul.urls')),
    path('derivee/', include('derivee.urls')),
    path('fonction/', include('fonction.urls')),
    path('compte/', include('compte.urls') ),
    path('polynome/', include('polynome.urls')),
    path('cours/', include('cours.urls'))
]