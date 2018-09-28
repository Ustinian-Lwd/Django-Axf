from django.shortcuts import render

# Create your views here.


# 首页
from app.models import Wheel, Nav, Mustbuy, Shop, MainShow


def home(request):
    # 网页标题
    title = '首页'
    # 轮播图数据
    wheels = Wheel.objects.all()
    # 导航栏数据
    navs = Nav.objects.all()
    # 每日必购数据
    mustbuys = Mustbuy.objects.all()

    # 商品部分
    shoplist = Shop.objects.all()
    shophead = shoplist[0]
    shoptab = shoplist[1:3]
    shopclass = shoplist[3:7]
    shopcommend = shoplist[7:11]

    # 商品主体
    mainshows = MainShow.objects.all()


    return render(request, 'home.html', context={
        'title': title,
        # 轮播图
        'wheels': wheels,
        # 导航
        'navs': navs,
        # 每次必购
        'mustbuys': mustbuys,
        # 商品部分
        'shophead': shophead,
        'shoptab': shoptab,
        'shopclass': shopclass,
        'shopcommend': shopcommend,
        # 商品主体
        'mainshows': mainshows,

    })


# 闪购
def market(request):
    title = '闪购'
    return render(request, 'market.html', context={
        'title': title,

    })


# 购物车
def cart(request):
    title = '购物车'
    return render(request, 'cart.html', context={
        'title': title,


    })


# 我的
def mine(request):
    title = '我的'
    return render(request, 'mine.html', context={
        'title': title,
    })

