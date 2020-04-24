from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from .serializers import UserModelSerializer
from .models import UserProfiles as User
from rest_framework.mixins import CreateModelMixin
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

# CreateModelMixin,viewsets.GenericViewSet
class UserViewset(CreateAPIView):
    # 用户注册时候的验证
    serializer_class = UserModelSerializer
    queryset = User.objects.all()


    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True) # 具有raise_exception异常标志，如果存在验证错误将会抛出一个serializers.ValidationError异常。
        user = self.perform_create(serializer)
        res_dict = serializer.data


        from rest_framework_jwt.settings import api_settings

        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        
        payload = jwt_payload_handler(user)
        res_dict["token"] = jwt_encode_handler(payload)
        res_dict["username"] = user.username

        headers = self.get_success_headers(serializer.data)

        return Response(res_dict, status=status.HTTP_201_CREATED, headers=headers)

    
    def perform_create(self, serializer):
        return serializer.save()


# SmsCodeViewset 生成验证码




""" 用户的操作：注册、登录、退出、忘记密码 """
