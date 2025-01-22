from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.views.generic import View
from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm

#회원가입 뷰 구현현
class SignUpView(View):  #회원가입을 위한 뷰 클래스 
    def get(self,request): #회원가입 폼을 보여주는 역할 
        form = SignUpForm()
        return render(request, 'user/signup.html', {'form': form})


    def post(self, request):
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid(): #폼의 유효성 검사 
            user = form.save() #if문 제어=> 유효한 경우 사용자를 데이터베이스에 저장 
            login(request, user) #사용자 로그인 처리 
            return redirect('post_list') #회원가입 후 게시글 목록 페이지로 이동 

#로그인 및 로그아웃 구현 

#로그인 구현
class LoginView(View): #로그인 페이지의 요청을 처리(로그인 화면 표시 사용자 인증 후 세션 생성)
    def get(self, request):
        form = AuthenticationForm()   #장고에서 제공하는 기본 로그인 폼(빈 폼을 생성 후 템플릿으로 전달)
        return render(request,'user/login.html', {'form': form} )
    
    def post(self, request):
        #로그인 폼 데이터를 받아 AuthentificationForm에 전달
        form = Authentication(data=request.POST)

        if form.is_valid(): #유효성 검사
            user = form.get_user() #사용자 객체 가져오기
            login(request, user) #로그인 수행 
            return redirect('post_list') #로그인 성공 시 게시글 목록 페이지로 이동

        #실패 시 다시 로그인 폼을 렌더링
        return render(request,'user/login.html', {'form': form})     

class Logoutview(View):
    def get(self, request):
        logout(request) #현재 섹션 삭제 
        return redirect('login') #로그아웃 후 로그인 페이지로 리디렉션 

        