from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=30)
    audience = models.IntegerField()
    poster_url = models.CharField(max_length=500)
    description = models.TextField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='movies')
    
    def __str__(self):
        return self.title


class Score(models.Model):
    content = models.CharField(max_length=50)
    score = models.IntegerField(
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ])
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.id}번 : {self.content} {self.score}"
    
    