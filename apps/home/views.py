from django.shortcuts import render
from rest_framework import generics

from .models import BigGoodsTag, SmallGoodsTag
from .serializers import BigTagsSerilizer, SmallTagsSerilizer

# 大分类
class BigTagsList(generics.ListAPIView):
    queryset = BigGoodsTag.objects.all()
    serializer_class = BigTagsSerilizer

class BigTagsDetail(generics.RetrieveAPIView):
    queryset = BigGoodsTag.objects.all()
    serializer_class = BigTagsSerilizer

# 小分类
class SmallTagsList(generics.ListAPIView):
    queryset = SmallGoodsTag.objects.all()
    serializer_class = SmallTagsSerilizer

class SmallTagsDetail(generics.RetrieveAPIView):
    queryset = SmallGoodsTag.objects.all()
    serializer_class = SmallTagsSerilizer