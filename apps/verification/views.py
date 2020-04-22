import random

from django.shortcuts import render
from django.http import JsonResponse
from utils.yuntongxun.sms import CCP
from django_redis import get_redis_connection
from rest_framework.views import APIView

class SMSAPIView(APIView):
    # url: users/sms/(?P<mobile>1[3-9]\d{9})
    def get(self,request,mobile):
        redis = get_redis_connection("sms_codes")
        # 获取短信发送间隔
        try:
            interval = redis.get("%s_interval" % mobile)
            if interval:
                print(interval)
                return JsonResponse({'result':'-1'})
        except:
            pass

        ccp = CCP()
        sms_codes = "%04d" % random.randint(1,9999)
        result = ccp.send_template_sms(mobile,[sms_codes, 5],1)

        if not result:
            """发送成功"""
            redis.setex("%s_sms_codes" % mobile, 5*60, sms_codes)
            # 这里的值不重要,重要的是这个变量是否在redis被查找到
            redis.setex("%s_interval" % mobile, 60, 1)

        return JsonResponse({"result":result})
