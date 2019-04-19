from django import forms
from .models import Score

class ScoreForm(forms.ModelForm):
    content = forms.CharField(max_length=50)
    value = forms.IntegerField(min_value=1, max_value=5)
    class Meta:
        model = Score
        fields = ['content', 'value']