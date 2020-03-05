from django.db import models

# Create your models here.
# 由于大类别模型和小类别模型并没有涉及到用户表的外键依赖，先练练手
""" 大类别模型 """
class BigGoodsTag(models.Model):
    name = models.CharField(max_length=20)
    create_time = models.DateTimeField(auto_now_add=True)
    is_delete = models.BooleanField(default=False)

    class Meta:
        db_table = 'big_goods_tag'
    
    def __str__(self):
        return self.name


""" 小类别模型 """
class SmallGoodsTag(models.Model):
    name = models.CharField(max_length=20)
    create_time = models.DateTimeField(auto_now_add=True)
    is_delete = models.BooleanField(default=False)
    # 定义外键和一对一关系的时候需要加on_delete选项，此参数为了避免两个表里的数据不一致问题
    big_tag = models.ForeignKey('BigGoodsTag',on_delete = models.CASCADE)

    class Meta:
        db_table = 'small_goods_tag'
    
    def __str__(self):
        return self.name