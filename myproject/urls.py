from django.contrib import admin #관리자 페이지 
from django.urls import path  #url 설정 모듈 

urlpatterns = [
    path('admin/', admin.site.urls),  #관리자 페이지 url
    path('user/', include ('user.urls')), #user 앱 url포함 
]
