from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import Profile
from django import forms


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        # UserCreationForm에 있는 Meta 클래스의 fields를 그대로 쓰겠다
        # fields = UserCreationForm.Meta.fields


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        # User를 수정할 수 있게 하면 안 됨
        fields = ['nickname', 'description', 'image']