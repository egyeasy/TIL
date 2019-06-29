from django import forms
from .models import Shout


class ShoutForm(forms.Form):
    title = forms.CharField(max_length=30)
    content = forms.CharField(max_length=100)


class ShoutModelForm(forms.ModelForm):
    class Meta:  # 메타 정보를 넣어줌
        model = Shout
        # form의 필드 중 어떤 것을 쓸지 얘기해준다
        fields = '__all__'  # 모든 필드 사용
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-control'
            })
        }
