from django.contrib.auth.backends import ModelBackend
from .models import UserProfiles as User
from django.db.models import Q
# from django.contrib.auth import authenticate
# from django.contrib.auth.hashers import check_password
import re

def get_user_by_account(account):
    """根据账号信息获取用户模型"""
    try:
        # if re.match('^1[3-9]\d{9}$', account):
        #     # 手机号
        #     user = User.objects.get(mobile=account)
        # else:
        #     # 用户名
        #     user = User.objects.get(username=account)

        user = User.objects.get(Q(mobile=account) | Q(username=account))

    except User.DoesNotExist:
        user = None

    return user


class UsernameMobileAuthBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        # 进行登录判断
        user = get_user_by_account(username)

        print('-----')
        print(user.check_password(password))
        print(password)
        print('-----')
        # 目前的问题是：user.check_password(password) 的结果为 False 原因是？
        # print(check_password(password, user.password))
        # 账号通过了还要进行密码的验证,以及判断当前站好是否是激活状态
        if isinstance(user,User) and user.check_password(password) and self.user_can_authenticate(user):
            print('hi')
            return user



def jwt_response_payload_handler(token, user=None, request=None):
    """
    自定义jwt认证成功返回数据
    """
    return {
        'msg': 'success',
        'status': 200,
        'data': {
            # data自定义你接口想返回的信息
            'token': token,
            'id': user.id,
            'username': user.username
        }
        
    }


def jwt_response_payload_error_handler(serializer, request = None):
    return {
        "msg": "用户名或者密码错误",
        "status": 400,
        "detail": serializer.errors
    }

