# 给xadmin设置基本站点配置信息
import xadmin
from xadmin import views

class BaseSetting(object):
    """xadmin的基本配置"""
    enable_themes = True  # 开启主题切换功能
    use_bootswatch = True

xadmin.site.register(views.BaseAdminView, BaseSetting)

class GlobalSettings(object):
    """xadmin的全局配置"""
    site_title = "校园二手交易平台"  # 设置站点标题
    # site_footer = ""  # 设置站点的页脚
    menu_style = "accordion"  # 设置菜单折叠

xadmin.site.register(views.CommAdminView, GlobalSettings)


# 轮播图
from .models import Banner
class BannerInfoModelAdmin(object):
    list_display=['image_url','priority','link_to','create_date','is_delete']
xadmin.site.register(Banner, BannerInfoModelAdmin)

# 大分类
from .models import BigGoodsTag
class BigGoodsTagModelAdmin(object):
    """大类别管理类"""
    pass
xadmin.site.register(BigGoodsTag, BigGoodsTagModelAdmin)


# 小分类
from .models import SmallGoodsTag
class SmallGoodsTagModelAdmin(object):
    """小类别管理类"""
    pass
xadmin.site.register(SmallGoodsTag, SmallGoodsTagModelAdmin)