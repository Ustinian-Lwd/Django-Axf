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
    # 注册
    url(r'^register', views.register, name='register'),
    # 登录
    url(r'^login/$', views.login, name='login'),
    # 退出
    url(r'^logout/$', views.exituser, name='logout'),
    # 检验用户名
    url(r'^checkuser/$', views.checkuser, name='checkuser'),
    # 购物车
    url(r'^cart/$', views.cart, name='cart'),
    # 添加购物车
    url(r'^addcart/$', views.addcart, name='addcart'),
    # 删减购物车
    url(r'^subcart/$', views.subcsrt, name='subcart'),
    # 改变勾选的状态
    url(r'^changecartstatus/$', views.changecartstatus, name='changecartstatus'),
    # 全选状态
    url(r'^changecartselect/$', views.changecartselect, name='changecartselect')








]


