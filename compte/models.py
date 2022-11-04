from django.db import models
from django.contrib.auth.models import User

class parametreGraph(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    backgroud_color = models.CharField(max_length=7)
    fonction_color = models.CharField(max_length=7)
    grid = models.BooleanField()
    name_xaxis = models.CharField(max_length=50)
    name_yaxis = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.user.username   