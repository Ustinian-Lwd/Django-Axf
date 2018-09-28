import hashlib
import os
import uuid

from django.contrib.auth import logout
from django.http import JsonResponse
from django.shortcuts import render, redirect
from LwdAxf import settings
from app.models import Wheel, Nav, Mustbuy, Shop, MainShow, Foodtypes, Goods, User, Cart


####################### 首页　＃＃＃＃＃＃＃＃＃＃
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


    return render(request, 'home/home.html', context={
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


################ 闪购 #######################
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



    # 如何加数据？
    # 结合两张表
    #　第一，通过token的值，来判断当前用户的状态并且找到对应的user
    # 第二，通过user从ｃａｒｔ中找到对应的来设置对应的数量

    token = request.session.get('token')
    carts = []

    if token:
        user = User.objects.get(token=token)
        carts = Cart.objects.filter(user=user).exclude(number=0)


    return render(request, 'market/market.html', context={

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

        # 购物车模型
        'carts': carts,


    })






# 购物车
def cart(request):
    title = '购物车'
    return render(request, 'cart/cart.html', context={
        'title': title,


    })

# 添加到购物车
def addcart(request):
    # 思路
    # 将ajax请求的goodsid获取
    # 即当前用户点击的那个商品
    # goodsid
    #　找到对应的商品
    goodsid = request.GET.get('goodsid')
    print(goodsid)
    # 用户－－－
    token = request.session.get('token')

    responseData = {
        'msg': '',
        'status': ''
    }

    if token:  # 登录
        user = User.objects.get(token=token)
        print(user.name)
        goods = Goods.objects.get(pk=goodsid)
        print(goods.productname)

        carts = Cart.objects.filter(goods=goods).filter(user=user)
        if carts.exists():  # 存在
            #　取第一个
            cart = carts.first()
            cart.number = cart.number + 1
            #　如果库存数量比我添加的数据还要小
            #　那么添加的数据只能为库存数量
            if goods.storenums < cart.number:
                cart.number = goods.storenums
            cart.save()
            responseData['msg'] = '添加购物车成功'
            responseData['status'] = 1
            responseData['number'] = cart.number
            return JsonResponse(responseData)
        else:  # 不存在
            cart = Cart()
            cart.user = user
            cart.goods = goods
            cart.number = 1
            cart.save()

            responseData['msg'] = '添加购物车成功'
            responseData['status'] = 1
            responseData['number'] = cart.number
            return JsonResponse(responseData)

    else:  # 未登录
        # ajax请求操作，是重定向不了的！
        # return redirect('axf:login')

        responseData['msg'] = '请登录后操作'
        responseData['status'] = '-1'

        return JsonResponse(responseData)

    # return JsonResponse(responseData)








########################## 我的　########################
def mine(request):

    responseData = {
        'title': '我的'
    }
    # 获取session
    token = request.session.get('token')

    # 存在---->登录状态
    if token:
        user = User.objects.get(token=token)
        responseData['name'] = user.name
        responseData['rank'] = user.rank
        responseData['img'] = '/static/uploads/' + user.img
        responseData['islogin'] = True
    # 不存在---->
    else:
        responseData['name'] = '未登录'
        responseData['rank'] = '无'
        responseData['img'] = '/static/uploads/lwd.jpg'
        responseData['islogin'] = False

    return render(request, 'mine/mine.html', context=responseData)


# 加密
def generate_password(password):
    sha = hashlib.sha512()
    sha.update(password.encode('utf-8'))
    return sha.hexdigest()


# 注册
def register(request):
    # 注册
    if request.method == 'POST':
        # 基本信息
        user = User()
        user.account = request.POST.get('account')
        user.password = generate_password(request.POST.get('password'))
        user.name = request.POST.get('name')
        user.tel = request.POST.get('tel')
        user.address = request.POST.get('address')

        # 头像
        imgname = user.account + '.jpg'
        imgPath = os.path.join(settings.MEDIA_ROOT, imgname)
        # 获取文件
        file = request.FILES.get('file')
        # 打开文件
        fp = open(imgPath, 'wb')
        # 文件操作
        for i in file.chunks():
            fp.write(i)
        # 关闭文件
        fp.close()

        user.img = imgname

        # token
        user.token = str(uuid.uuid5(uuid.uuid4(), 'register'))

        # 保存写入数据
        user.save()

        # 状态保持
        request.session['token'] = user.token


        # 重定向
        response = redirect('axf:mine')

        return response

    elif request.method == 'GET':
        return render(request, 'mine/register.html')


# 登录
def login(request):
    # 登录
    if request.method == 'POST':
        account = request.POST.get('account')
        password = request.POST.get('password')
        # 异常
        #
        try:
            user = User.objects.get(account=account)
            if user.password != generate_password(password):  # 密码错误
                return render(request, 'mine/login.html', context={'error': '密码错误!'})
            else:  # 登录成功
                # 更新token
                user.token = str(uuid.uuid5(uuid.uuid4(), 'login'))
                user.save()
                # 状态保持
                request.session['token'] = user.token
                return redirect('axf:mine')
        except:
            return render(request, 'mine/login.html', context={'error': '用户名有误，请检查后输入!'})
    # 显示登录界面
    elif request.method == 'GET':
        return render(request, 'mine/login.html')



# 检验用户
def checkuser(request):
    account = request.GET.get('account')

    # get方法若不存在，将会报错
    # 存在，异常处理　try  ---->   用户名可用
    # 不存在，异常处理　except　---->   用户名可用
    try:
        user = User.objects.get(account=account)
        return JsonResponse({'msg': '用户名已存在!', 'status': '-1'})
    except:
        return JsonResponse({'msg': '用户名可用!', 'status': '1'})


# 退出用户
def exituser(request):
    logout(request)
    return redirect('axf:mine')


