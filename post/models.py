# post/models.py
from django.db import models  # Django의 모델 클래스 가져오기
from user.models import CustomUser  # 사용자 모델 임포트

# 게시글(Post) 모델 정의
class Post(models.Model):
    title = models.CharField(max_length=200)  # 제목 필드, 최대 길이 200
    content = models.TextField()  # 내용 필드 (제한 없음)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # 작성자 (외래 키)
    created_at = models.DateTimeField(auto_now_add=True)  # 생성 시간 (자동 저장)
    updated_at = models.DateTimeField(auto_now=True)  # 수정 시간 (자동 갱신)
