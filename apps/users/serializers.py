""" from rest_framework import serializers
from .models import UserProfiles

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfiles
        fields = ('id','username') """

# 尝试实现注册/登录 施工中

