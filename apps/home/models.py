from django.db import models

# Create your models here.
# 由于大类别模型和小类别模型并没有涉及到用户表的外键依赖，先练练手，此做法严重错误，请勿模仿
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
    big_tag = models.ForeignKey('BigGoodsTag', on_delete=models.CASCADE)

    class Meta:
        db_table = 'small_goods_tag'

    def __str__(self):
        return self.name


""" 物品模型 √ """


class Goods(models.Model):
    order_id = models.CharField(max_length=30)
    name = models.CharField(max_length=20)
    desc = models.CharField(max_length=200)
    # 物品图片保存路径
    thumbnail_url = models.URLField()
    price = models.FloatField()
    publish_time = models.DateTimeField(auto_now_add=True)
    is_delete = models.BooleanField(default=False)

    # 数量  点击数
    number = models.IntegerField(default=1)
    clicks = models.IntegerField(default=0)
    is_buy = models.BooleanField(default=False)  # 默认未交易

    small_tag = models.ForeignKey('SmallGoodsTag', on_delete=models.CASCADE)
    author = models.ForeignKey('users.UserProfiles', on_delete=models.CASCADE)

    def increase_click(self):
        self.clicks += 1
        self.save(update_fields=['clicks'])

    class Meta:
        db_table = 'goods'
        # 按发布时间降序排列，-表示降序
        ordering = ['-publish_time', ]


""" 购物车模型 √ """


class Cart(models.Model):
    create_time = models.DateTimeField(auto_now_add=True)
    is_delete = models.BooleanField(default=False)

    author = models.ForeignKey('users.UserProfiles', on_delete=models.CASCADE)
    goods = models.ForeignKey('Goods', on_delete=models.CASCADE)

    class Meta:
        db_table = 'tb_cart'
        # 按创建时间降序排列，-表示降序
        ordering = ['-create_time', ]


""" 收藏表模型 √ """


class Keep(models.Model):
    create_time = models.DateTimeField(auto_now_add=True)
    is_delete = models.BooleanField(default=False)

    author = models.ForeignKey('users.UserProfiles', on_delete=models.CASCADE)
    goods = models.ForeignKey('Goods', on_delete=models.CASCADE)

    class Meta:
        db_table = 'tb_keep'
        ordering = ['-create_time', ]


""" 我的订单模型 √ """


class MyOrder(models.Model):
    create_time = models.DateTimeField(auto_now_add=True)
    is_delete = models.BooleanField(default=False)
    # 是否发货  默认未发货
    is_shop = models.BooleanField(default=False)
    # 购买数量
    number = models.IntegerField(default=1)

    author = models.ForeignKey('users.UserProfiles', on_delete=models.CASCADE)
    goods = models.ForeignKey('Goods', on_delete=models.CASCADE)

    class Meta:
        db_table = 'tb_my_order'
        ordering = ['-create_time', ]


""" 物品评论模型 √ """


class Comment(models.Model):
    create_time = models.DateTimeField(auto_now_add=True)
    is_delete = models.BooleanField(default=False)
    content = models.CharField(max_length=300)

    author = models.ForeignKey('users.UserProfiles', on_delete=models.CASCADE)
    goods = models.ForeignKey('Goods', on_delete=models.CASCADE)
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True)

    def to_dict_data(self):
        comment_dict = {
            'goods_id': self.goods.id,
            'content_id': self.id,
            'content': self.content,
            'author': self.author.username,
            'create_time': self.create_time.strftime('%Y/%m/%d %H:%M'),
            'parent': self.parent.to_dict_data() if self.parent else None,
        }
        return comment_dict

    class Meta:
        db_table = 'tb_comment'
        ordering = ['-create_time', ]



'''轮播图模型'''
class Banner(models.Model):
    image_url = models.URLField()
    priority = models.IntegerField()
    link_to = models.URLField()
    create_date = models.DateTimeField(auto_now_add=True)
    is_delete = models.BooleanField(default=False)

    class Meta:
        db_table='banner'
        ordering = ['-priority']

# 考虑中
""" 轮播图模型、热搜排行、trade 交易 如何解决商品支付
用户收藏、用户收货、用户留言 """