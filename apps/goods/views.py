# from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status






""" class GoodsListView(APIView):
    '''物品详细信息'''
    def get(self,request,good_id):


    def get(self,request,good_id):
        good=Goods.objects.select_related('author').only('id','author__username','clicks').filter(is_delete = False,id = good_id,is_buy = False)
        if good.exists():
            comments=Comment.objects.select_related('goods','author').only('content','goods__name','author__username','parent__author','parent__content').filter(is_delete = False,goods_id = good_id)
            # 评论数量
            comments_num=comments.count()
            # comments_num=comments_num if comments_num else 0
            # 更新点击数
            clicks=good.first().clicks+1
            good.update(clicks=clicks)
            good=good.first()
            
            # return render(request,'goods/goods_detail.html',locals())
        return json_status.params_error(message = '物品不存在') """