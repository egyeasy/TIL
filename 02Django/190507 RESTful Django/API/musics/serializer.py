from rest_framework import serializers  # from django import forms 와 비슷
from .models import Music


class MusicSerializer(serializers.ModelSerializer):  # class MusicForm(forms.ModelForm)
    class Meta:  # ModelForm과 똑같은 방식으로 만든다.
        model = Music
        fields = ['id', 'title', 'artist',]  # API 응답은 id도 같이 넘겨줘야 한다.