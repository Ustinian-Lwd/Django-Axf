from django.db import models

# Create your models here.

# 基础 类
class Base(models.Model):
    img = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    trackid = models.CharField(max_length=20)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name



######################## [首页] ########################

# 轮播图
class Wheel(Base):
    class Meta:
        db_table = 'axf_wheel'


# 导航栏
class Nav(Base):
    class Meta:
        db_table = 'axf_nav'


# 每日必购
class Mustbuy(Base):
    class Meta:
        db_table = 'axf_mustbuy'



# 商品部分内容
# showhead
# showtab
# showclass
# 商品推荐
class Shop(Base):
    class Meta:
        db_table = 'axf_shop'




# 商品主体　
class MainShow(models.Model):

    # 理解
    # 一大类
    # 产品ID
    trackid = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    img = models.CharField(max_length=200)
    # 分类id
    categoryid = models.CharField(max_length=10)
    brandname = models.CharField(max_length=50)


    # 小西瓜--
    # 路径
    img1 = models.CharField(max_length=200)
    # 子类id
    childcid1 = models.CharField(max_length=10)
    # 西瓜产品的id
    productid1 = models.CharField(max_length=10)
    # 长名字
    longname1 = models.CharField(max_length=200)
    # 优惠价
    price1 = models.FloatField()
    # 市场价格【原价】
    marketprice1 = models.FloatField()


    # 火龙果--
    img2 = models.CharField(max_length=200)
    childcid2 = models.CharField(max_length=10)
    productid2 = models.CharField(max_length=10)
    longname2 = models.CharField(max_length=200)
    price2 = models.FloatField()
    marketprice2 = models.FloatField()

    # 番茄--
    img3 = models.CharField(max_length=200)
    childcid3 = models.CharField(max_length=10)
    productid3 = models.CharField(max_length=10)
    longname3 = models.CharField(max_length=200)
    price3 = models.FloatField()
    marketprice3 = models.FloatField()

    class Meta:
        db_table='axf_mainshow'




######################## [闪购] ########################

# 商品分类  比如侧边栏等以及顶部栏中全部分类的数据
class Foodtypes(models.Model):
    # 分类id
    typeid = models.CharField(max_length=10)
    # 分类名称--热销榜-----
    typename = models.CharField(max_length=100)
    # 子类名称--
    childtypenames = models.CharField(max_length=200)
    # 分类排序(显示的先后顺序)
    typesort = models.IntegerField()

    class Meta:
        db_table = 'axf_foodtypes'

    def __str__(self):
        return self.typename


# 全部商品即需要显示的内容
class Goods(models.Model):
    # 商品id
    productid = models.CharField(max_length=10)
    # 商品图片
    productimg = models.CharField(max_length=255)
    # 商品名称--简称
    productname = models.CharField(max_length=100)
    # 商品长名字--一大串
    productlongname = models.CharField(max_length=255)
    # 精选--是否为精选,有则显示,无则
    isxf = models.BooleanField(default=False)
    # 买一送一
    pmdesc = models.BooleanField(default=False)
    # 规格--例如牛奶多少毫升
    specifics = models.BooleanField(max_length=100)
    # 价格
    price = models.FloatField()
    # 超市价格
    marketprice = models.FloatField()
    # 分类id
    categoryid = models.CharField(max_length=10)
    # 子类id
    childcid = models.CharField(max_length=10)
    # 子类名字
    childcidname = models.CharField(max_length=50)
    # 详情id
    dealerid = models.CharField(max_length=10)
    # 库存量
    storenums = models.IntegerField()
    # 销售量
    productnum = models.IntegerField()

    class Meta:
        db_table = 'axf_goods'


# 用户　模型类
class User(models.Model):
    # 账号
    account = models.CharField(max_length=20, unique=True)
    # 密码
    password = models.CharField(max_length=256)
    # 名字
    name = models.CharField(max_length=100)
    # 电话
    tel = models.CharField(max_length=20)
    # 地址
    address = models.CharField(max_length=256)
    # 头像
    img = models.CharField(max_length=100)
    # 等级
    rank = models.IntegerField(default=1)
    # token
    token = models.CharField(max_length=100)

    class Meta:
        db_table = 'axf_user'


# 购物车 模型类
class Cart(models.Model):
    # 用户
    user = models.ForeignKey(User)
    # 商品
    goods = models.ForeignKey(Goods)
    # 选择数量
    number = models.IntegerField(default=1)
    # 是否选中
    isselect = models.BooleanField(default=True)

    class Meta:
        db_table = 'axf_cart'


