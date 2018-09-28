from django.conf.urls import url
from app import views


# 路由
urlpatterns = [
    # 首页
    url(r'^$', views.home, name='home'),
    # 首页
    url(r'^home/$', views.home, name='home'),
    # 闪购
    url(r'^market/(\d+)/(\d+)/(\d+)/$', views.market, name='market'),
    # 购物车
    url(r'^cart/$', views.cart, name='cart'),
    # 我的
    url(r'^mine/$', views.mine, name='mine'),




]


