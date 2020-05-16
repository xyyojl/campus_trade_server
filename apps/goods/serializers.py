from rest_framework import serializers

from apps.home.serializers import SmallTagsSerilizer
from apps.users.serializers import UserModelSerializer


class GoodsSerializer(serializers.ModelSerializer):
    small_tag=SmallTagsSerilizer()
    author=UserModelSerializer()
    class Meta:
        fields=('id','order_id','name','desc','thumbnail_url','price','publish_time','small_tag','author')