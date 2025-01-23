from django.contrib.auth.forms import UserCreationForm  # 회원가입 폼 제공
from .models import CustomUser  # 사용자 모델 가져오기

class SignUpForm(UserCreationForm):  # 사용자 입력 데이터를 수집 및 검증 
    class Meta:  # 특정 Django 모델의 설정 정보(메타데이터)를 정의
        model = CustomUser  # 사용자 모델 설정
        fields = ['username', 'email', 'password1', 'password2', 'profile_image', 'bio']


        
