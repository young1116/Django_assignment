from django.contrib.auth.models import AbstractUser #기본 사용자 모델 확장용
                                                  #AbtractUser: Django의 기본 사용자 모델울 상속받아 필드를 추가할 때 사용.
from django.db import models  #Django의 ORM사용 (데이터베이스와 상호작용 할 수 있는 ORM)

# Create your models here.

class CustomUser(AbstractUser): #사용자 모델을 커스터마이징
    profile_image = models.ImageField(upload_to = 'profile_pics/', null=True, blank=True)
    bio = models.TextField(max_length=500, null=True, blank=True)        


