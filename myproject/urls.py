from django.contrib import admin  # 관리자 페이지
from django.urls import include, path  # URL 설정 모듈

urlpatterns = [
    path('admin/', admin.site.urls),  # 관리자 페이지 URL
    path('user/', include('user.urls')), #user 앱 URL 포함 
    path('post/', include('post.urls')),  # post 앱 URL 포함  
]
