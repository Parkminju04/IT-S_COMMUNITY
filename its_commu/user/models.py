from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
# Create your models here.

class MyAccountManager(BaseUserManager):
    # 일반 user 생성, id 가 userID를 의미함
    def create_user(self, id, name, std_id, birth, tel, email, github, password=None):
        if not id:
            raise ValueError("Users must have an userID.")
        if not name:
            raise ValueError("Users must have an name.")
        user = self.model(
            id=id,
            name=name,
            std_id=std_id,
            birth=birth,
            tel=tel,
            email=self.normalize_email(email),
            github=github
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    # 관리자 User 생성
    def create_superuser(self, id, name, std_id, birth, tel, email, github, password, **extra_fields):
        user = self.create_user(
            id=id,
            name=name,
            std_id=std_id,
            birth=birth,
            tel=tel,
            email=email,
            github=github,
            password=password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save(using=self._db)
        return user


class User(models.Model):
    id = models.CharField(max_length=20, null=False)
    pw = models.CharField(max_length=255, null=False)
    name = models.CharField(max_length=50, null=False, unique=True)
    std_id = models.CharField(max_length=20, primary_key=True, null=False)
    birth = models.DateField(null=False)
    tel = models.CharField(max_length=50, null=False)
    email = models.CharField(max_length=50, null=False)
    github = models.CharField(max_length=50)
    in_date = models.DateField(null=False)
    type = models.CharField(max_length=50)
    info = models.CharField(max_length=255)
    insert_date = models.DateField(auto_now_add=True)
    insert_user = models.CharField(max_length=50)
    deleted = models.CharField(max_length=1)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    object = MyAccountManager()  # 헬퍼 클래스 사용

    ID_FIELD = 'id'  # 로그인 ID로 사용할 필드
    REQUIRED_FIELDS = ['name', 'std_id', 'birth', 'tel', 'email', 'github']  # 필수 작성 필드

    def __str__(self):
        return self.id

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_lable):
        return True
