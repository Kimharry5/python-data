from django.db import models
from django.contrib.auth.models import User

class Movie(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    genres = models.CharField(max_length=500)
    likes = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    count = models.IntegerField(default=0)