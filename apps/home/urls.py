from django.urls import path
from . import views

urlpatterns = [
    path('banner/',views.BannerInfoListAPIView.as_view()),
    # path('bigtags/list/', views.BigTagsList.as_view()),
    # path('bigtags/<int:pk>/',views.BigTagsDetail.as_view()),
    # path('smalltags/list/', views.SmallTagsList.as_view()),
    # path('smalltags/<int:pk>/',views.SmallTagsDetail.as_view()),
]