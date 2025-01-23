# post/forms.py
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post  # Post 모델과 연결
        fields = ['title', 'content']  # 사용자에게 입력받을 필드 지정





