# from django.db.models import Q  # 对对象进行复杂查询，并支持&（and）,|（or），~（not）操作符
from rest_framework.generics import ListAPIView
from .models import Banner,BigGoodsTag, SmallGoodsTag
from .serializers import BannerSerializer,BigTagsSerilizer, SmallTagsSerilizer

class BannerInfoListAPIView(ListAPIView):
    """ 轮播图列表 """
    queryset = Banner.objects.all() # Banner 模型类
    serializer_class = BannerSerializer 

class BigTagsInfoListAPIView(ListAPIView):
    queryset = BigGoodsTag.objects.all()
    serializer_class = BigTagsSerilizer

class SmallTagsInfoListAPIView(ListAPIView):
    queryset = SmallGoodsTag.objects.all()
    serializer_class = SmallTagsSerilizer




""" @require_GET   # /home/banner/list/
# @method_decorator(cache_page(timeout=120,cache='page_cache'))
def banner_list(request):
    '''返回轮播图列表'''
    banners=Banner.objects.filter(is_delete = False)
    serializer=BannerSerializer(banners,many=True)
    return json_status.result(data = {'banners':serializer.data}) """









""" from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import generics
from rest_framework import viewsets

from .models import BigGoodsTag, SmallGoodsTag,Goods
from .serializers import BigTagsSerilizer, SmallTagsSerilizer,GoodsSerializer
from rest_framework.pagination import PageNumberPagination """
# from goods.serializers import GoodsSerializer



""" # 大分类
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


class BigCategoryViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = BigGoodsTag.objects.all()
    serializer_class = BigTagsSerilizer """


# 施工中 test

# 商品列表自定义分页
""" class GoodsPagination(PageNumberPagination):
    #默认每页显示的个数
    page_size = 20
    #可以动态改变每页显示的个数
    page_size_query_param = 'page_size'
    #页码参数
    page_query_param = 'page'
    #最多能显示多少页
    max_page_size = 100


class GoodsListViewSet(mixins.ListModelMixin,viewsets.GenericViewSet):
    # 分页
    pagination_class = GoodsPagination
    # 这里必须要定义一个默认的排序,否则会报错
    queryset = Goods.objects.all().order_by('publish_time')
    serializer_class = GoodsSerializer
 """