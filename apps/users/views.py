from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from .serializers import UserModelSerializer
from .models import UserProfiles as User

class UserAPIView(CreateAPIView):
    serializer_class = UserModelSerializer
    queryset = User.objects.all()



# Create your views here.

""" 用户的操作：注册、登录、退出、忘记密码 """
