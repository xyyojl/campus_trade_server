from rest_framework import serializers
from .models import UserProfiles as User
import re
from django_redis import get_redis_connection

class UserModelSerializer(serializers.ModelSerializer):
    # 施工中 需要根据实际情况修改
    # 短信验证码的 max_length 可能会改
    sms_codes = serializers.CharField(write_only=True, max_length=4,min_length=4,required=True,help_text="短信验证码")
    password2 = serializers.CharField(write_only=True,help_text="确认密码")
    token = serializers.CharField(read_only=True,help_text="jwt token值")
    # 获取到 User 的序列器
    class Meta:
        model = User
        # 用户名、密码、学校名称、电话号码
        fields = ["mobile","id","token","password","password2","username","sms_codes",'school']
        # 使用extra_kwargs选项快捷地在字段上指定任意附加的关键字参数
        extra_kwargs = {
            "id":{"read_only":True},
            "username":{"write_only":True},
            "password":{"write_only":True},
            "mobile":{"write_only":True}
        }


    def validate_mobile(self, mobile):
        # 验证格式
        result = re.match('^1[3-9]\d{9}$', mobile)
        if not result:
            raise serializers.ValidationError("手机号码格式有误!")

        # 验证唯一性
        try:
            user = User.objects.get(mobile=mobile)
            if user:
                raise serializers.ValidationError("当前手机号码已经被注册!")

        except User.DoesNotExist:
            pass

        return mobile
    
    def validate(self, attrs):

        # 判断密码长度
        password = attrs.get("password")
        if not re.match('^.{6,16}$', password):
            raise serializers.ValidationError("密码长度必须在6-16位之间!")

        # 判断密码和确认密码是否一致
        password2 = attrs.get("password2")
        if password != password2:
            raise serializers.ValidationError("密码和确认密码不一致!")

        # 验证短信验证码
        mobile = attrs.get("mobile")
        redis = get_redis_connection("sms_codes")

        try:
            real_sms_codes = redis.get("%s_sms_codes" % mobile).decode()
        except:
            raise serializers.ValidationError("验证码不存在,或已经过期!")

        if real_sms_codes != attrs.get("sms_codes"):
            raise serializers.ValidationError("验证码不存在,或错误!")

        # 删除本次使用的验证码
        try:
            redis.delete("%s_sms_codes" % mobile)
        except:
            pass

        return attrs

    def create(self, validated_data):
        """保存用户"""
        username = validated_data.get("username")
        password = validated_data.get("password")
        school = validated_data.get("school")
        mobile = validated_data.get("mobile")

        try:
            user = User.objects.create_user(
                mobile=mobile,
                username=username,
                password=password,
                school=school
            )

            # 密码加密
            user.set_password(user.password)
            user.save()

        except:
            raise serializers.ValidationError("注册用户失败!")

        # 生成一个jwt
        from rest_framework_jwt.settings import api_settings

        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(user)
        user.token = jwt_encode_handler(payload)

        return user



# 待销毁
""" from rest_framework import serializers
from .models import UserProfiles

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfiles
        fields = ('id','username') """

# 尝试实现注册/登录 施工中

