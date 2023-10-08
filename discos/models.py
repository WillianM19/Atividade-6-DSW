from django.db import models

class Artist(models.Model):
    artist_name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.artist_name
    
class phonographicLabel(models.Model):
    phonographicLabel_name = models.CharField(max_length=50, default="vazio")
    
    def __str__(self):
        return self.phonographicLabel_name

class disc(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=800)
    phonographicLabel = models.ForeignKey(phonographicLabel, on_delete=models.CASCADE)
    year = models.IntegerField()
    country = models.CharField(max_length=20)
    genre = models.CharField(max_length=20)
    amount = models.IntegerField()
    artist = models.ManyToManyField(Artist)
    
    def __str__(self):
        return self.name

    
