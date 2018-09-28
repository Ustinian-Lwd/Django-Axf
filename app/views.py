from django.shortcuts import render

# Create your views here.

# 首页
from app.models import Wheel, Nav, Mustbuy, Shop, MainShow, Foodtypes, Goods


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
def market(request, categoryid, childid, sortid):

    # 闪购 标题
    title = '闪购'

    # 侧边栏的数据  热销榜  新品尝鲜
    foodtypes = Foodtypes.objects.all()

    # 测试 商品数据是否能够显示
    # goods = Goods.objects.all()[1:10]

    # 获取点击的分类下标,点击历史
    # kindIndex
    # 若存在kindIndex,则获取
    # 不存在,则默认为零,即展示首页的东西
    # kindIndex = int(request.COOKIES.get('kindIndex', 0))
    # 通过下标来获取对应的种类id--分类id
    # kindid = foodtypes[kindIndex].typeid

    typeIndex = int(request.COOKIES.get('typeIndex', 0))
    print(foodtypes[typeIndex])
    categoryid = foodtypes[typeIndex].typeid


    # 子类
    # 对应类下, 子类字符串
    # 全部分类下需要显示的数据
    # childtypenames = foodtypes.get(typeid=kindid).childtypenames
    # childlist = []
    # for item in childtypenames.split('#'):
    #     arr = item.split(':')
    #     obj = {'childname': arr[0], 'childid': arr[1]}
    #     childlist.append(obj)

    childtypenames = foodtypes.get(typeid=categoryid).childtypenames  # 对应分类下 子类字符串
    childlist = []
    for item in childtypenames.split('#'):
        arr = item.split(':')
        obj = {'childname': arr[0], 'childid': arr[1]}
        childlist.append(obj)


        # 根据商品分类 数据过滤
    # if childid == '0':  # 全部分类
    #     goodslist = Goods.objects.filter(categoryid=kindid)
    # else:  # 对应分类
    #     goodslist = Goods.objects.filter(categoryid=kindid, childcid=childid)

    if childid == '0':  # 全部分类
        goodslist = Goods.objects.filter(categoryid=categoryid)
    else:  # 对应分类
        goodslist = Goods.objects.filter(categoryid=categoryid, childcid=childid)



    # 排序处理
    # 销量排序
    if sortid == '1':
        goodslist = goodslist.order_by('productnum')
    # 价格最低
    elif sortid == '2':
        goodslist = goodslist.order_by('price')
    # 价格最高
    elif sortid == '3':
        goodslist = goodslist.order_by('-price')




    return render(request, 'market.html', context={

        'title': title,

        # 分类--热销榜等---
        'foodtypes': foodtypes,

        # 测试数据,商品是否显示
        # 'goods': goods,

        # 分类id,传过去给反向解析
        'categoryid': categoryid,

        # 子类id
        'childid': childid,

        # 数据列表---全部的商品
        'goodslist': goodslist,

        # 根据  类别展示商品
        'childlist': childlist,


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

