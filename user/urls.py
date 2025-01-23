from django.urls import path #url 경로 설정 모듈
from .views import SignUpView, LoginView, LogutView #뷰 가져오기 

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'), #회원가입 url
    path('login/', LoginView.as_view(), name='login'),    #로그인 url
    path('logout/', LogoutView.as_view(), name='logout'), #로그아웃 url
]
