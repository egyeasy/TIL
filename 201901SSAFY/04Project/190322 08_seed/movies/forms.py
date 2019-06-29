from django import forms
from django.db import models
from .models import Movie, Score


# class MovieForm(forms.Form):
#     title = forms.CharField(max_length=30)
#     audience = forms.IntegerField()
#     poster_url = forms.CharField(max_length=140)
#     description = forms.TextField()
#     genre_id = forms.ForeignKey(Genre, on_delete=models.CASCADE)


class MovieModelForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'

class ScoreModelForm(forms.ModelForm):
    class Meta:
        model = Score
        fields = ('content', 'score')