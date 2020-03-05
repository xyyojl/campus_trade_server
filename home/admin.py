from django.contrib import admin

# Register your models here.
from . models import BigGoodsTag, SmallGoodsTag
admin.site.register(BigGoodsTag)
admin.site.register(SmallGoodsTag)