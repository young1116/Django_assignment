from django.contrib.atuh.forms import UsercreationsForm #회원가입 폼 제공
from .models import CustomUser #사용자 모델 가져오기

class SignUpForm(UserCreationForm): #사용자 입력 데이터를 수집 및 검증 
    class Meta: #특정 Django 모델이나 폼의 **"설정 정보"** / 동작 방식의 설명을 제공하는 용도로 사용
                # "데이터에 대한 데이터(메타데이터)"를 정의하는 역할
        model = Customer
        fields = ['username','email','password1','password2','profile_image','bio']
