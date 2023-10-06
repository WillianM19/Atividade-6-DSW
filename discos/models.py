from django.db import models

class disc(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=800)
    phonographicLabel = models.CharField(max_length=200)
    year = models.IntegerField()
    country = models.CharField(max_length=20)
    genre = models.CharField(max_length=20)
    amount = models.IntegerField()