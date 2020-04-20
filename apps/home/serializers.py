from rest_framework import serializers
from .models import BigGoodsTag,SmallGoodsTag,Goods
from rest_framework.pagination import PageNumberPagination

""" class BigTagsSerilizer(serializers.ModelSerializer):

    class Meta:
        model = BigGoodsTag
        fields = ('id','name')

class SmallTagsSerilizer(serializers.ModelSerializer):
    # 覆盖外键字段
    big_tag = BigTagsSerilizer()

    class Meta:
        model = SmallGoodsTag
        fields = ('id','name','big_tag','is_delete') """

# Serializer实现商品列表页
""" class GoodsSerializer(serializers.Serializer):
    name = serializers.CharField(required=True,max_length=20)
    clicks = serializers.IntegerField(default=0)
    desc = serializers.CharField(max_length=200) """




# Goods 涉及到的外键 small_tag author

# 商品列表页
# 通过 serializers 的嵌套功能可以详细的显示分类的信息
""" class GoodsSerializer(serializers.ModelSerializer):
    # 差一个外键 author
    small_tag = SmallTagsSerilizer()
    class Meta:
        model = Goods
        fields = '__all__' """


