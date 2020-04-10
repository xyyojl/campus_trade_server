from django.db import models
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.models import AbstractUser, BaseUserManager, AbstractBaseUser, PermissionsMixin, UserManager as _UserManager

# 重点：重写用户模型

# 超级管理员
class UserManager(BaseUserManager):
    # 创建用户的公用方法
    def _create_user(self, username, password, **extra_fields):
        user = self.model(username = username, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    # 创建普通用户
    def create_user(self, username, password, **extra_fields):
        extra_fields['is_superuser'] = False
        extra_fields['is_staff'] = False
        return self._create_user(username, password, **extra_fields)

    # 创建超级管理员
    def create_superuser(self, username, password, **extra_fields):
        extra_fields['is_superuser'] = True
        extra_fields['is_staff'] = True
        return self._create_user(username, password, **extra_fields)
 
# 用户模型
class UserProfiles(AbstractBaseUser, PermissionsMixin):
    """ 用户信息 """
    username = models.CharField(max_length=20,unique=True,verbose_name="昵称",help_text="昵称",
                            error_messages={'unique': "此昵称已使用"}  
                            )
    school = models.CharField(max_length=12,verbose_name="学校",help_text="学校")
    address = models.CharField(max_length=40, blank=True)
    telephone = models.CharField(max_length=11, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_staff = models.BooleanField(blank = True)
    is_active = models.BooleanField(default = True)
    avatar = models.CharField(max_length=200)

    # 这是一个作为User的标识字段，所选的字段来代表这个用户
    USERNAME_FIELD = 'username'
    # 当创建用户时，这里面的字段都是必须输入的。
    # 错误：The field named as the 'USERNAME_FIELD' for a custom user model must not be included in 'REQUIRED_FIELDS'.
    # REQUIRED_FIELDS = ['username']

    objects = UserManager()


    class Meta:
        db_table = "tb_users"   
        verbose_name = "用户信息"    
        verbose_name_plural = verbose_name  

    def __str__(self): 
        return self.username



# 验证码 待完善
class VerifyCode(models.Model):
    """ 验证码 """
    code = models.CharField("验证码",max_length=10)
    mobile = models.CharField("电话",max_length=11)
    add_time = models.DateTimeField("添加时间",default=datetime.now)

    class Meta:
        db_table = "tb_users_verifycode"
        verbose_name = "短信验证"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.code
