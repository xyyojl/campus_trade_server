"""campus_trade_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework.documentation import include_docs_urls

# 添加xadmin的路由信息
import xadmin
xadmin.autodiscover()

# version模块自动注册需要版本控制的 Model
from xadmin.plugins import xversion
xversion.register_models()

""" from home.views import GoodsListViewSet, BigCategoryViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter() """

# 配置 goods 的 url
# router.register(r'goods', GoodsListViewSet)

# 配置Category的url
# router.register(r'categorys', BigCategoryViewSet, base_name="categorys")


urlpatterns = [
    path('admin/', admin.site.urls),
    # 注册总路由
    path('',include('home.urls')),
    path(r'xadmin/', xadmin.site.urls),
    # drf文档，title自定义
    # path('docs',include_docs_urls(title='校园二手交易平台')),
    # path('api-auth/',include('rest_framework.urls')),
    # 施工中
    #商品列表页
    # path('goods/',GoodsListView.as_view(),name='goods-list'),
    # path('api/v1/',include(router.urls)),
    # path('test/',include('home.urls')),
    # path('api/v1/',include('home.urls')),
    # token
    # path('api-token-auth/', views.obtain_auth_token),
    # jwt的token认证接口
    # path('login/', obtain_jwt_token )
]
