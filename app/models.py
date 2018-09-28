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


