from django.db import models
from django.contrib.auth.models import User

class Tags(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title

class Fiche(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    titre = models.CharField(max_length=50)
    description = models.TextField()
    tags = models.ManyToManyField(Tags)
    contenu = models.TextField()

    def __str__(self):
        return self.titre

class Liste(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    titre = models.CharField(max_length=50)
    description = models.TextField()
    tags = models.ManyToManyField(Tags)
    fiche = models.ManyToManyField(Fiche)

    def __str__(self):
        return self.titre