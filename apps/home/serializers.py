from rest_framework import serializers
# from . import models
from .models import BigGoodsTag,SmallGoodsTag

class BigTagsSerilizer(serializers.ModelSerializer):

    class Meta:
        model = BigGoodsTag
        fields = ('id','name')

class SmallTagsSerilizer(serializers.ModelSerializer):
    big_tag = BigTagsSerilizer()

    class Meta:
        model = SmallGoodsTag
        fields = ('id','name','big_tag','is_delete')