from django.contrib.auth.models import User
from django.db import models


class Categire(models.Model):
    categirie =models.CharField(max_length=30 ,null=True)

    def __str__(self):
        return self.categirie

class ProductModel(models.Model):
    product_id =models.IntegerField(null=True)
    product_name = models.CharField(max_length=100 ,null=True)
    product_price = models.CharField(max_length=30,null=True)
    product_categire = models.ForeignKey(Categire ,on_delete=models.CASCADE ,null=True)
    current_status = models.CharField(max_length=15 ,null=True)
    product_for = models.CharField(max_length=20 ,null=True)
    valid_upto = models.CharField(max_length=30,null=True)
    sizes =[('XSML' ,'XSML'),
           ('M', 'M'),
           ('SML' ,'SML'),
           ('L' ,'L'),
           ('XL' ,'XL'),
           ('XXl' ,'XXL'),
            ('7', '7'),
            ('8', '8'),
            ('9', '9'),
            ('10', '10'),
            ('11', '11'),

           ]
    product_image =models.ImageField(upload_to='products/' ,null=True)
    sizes =models.CharField(max_length=10 ,choices=sizes ,null=True)
    product_description =models.CharField(max_length=1000 ,null=True)

    def __str__(self):
        return self.product_name

class UserDetail(models.Model):
    usr=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    mobile=models.CharField(max_length=11,null=True)
    image=models.FileField(null=True)
    address=models.TextField(null=True)

    def __str__(self):
        return self.usr.username


class AddtocartModel(models.Model):
    usr=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    pro=models.ForeignKey(ProductModel,on_delete=models.CASCADE,null=True)
    quantity=models.IntegerField(null=True)
    total_price=models.FloatField(null=True)
    size=models.CharField(max_length=10,null=True)

    def __str__(self):
        return self.pro.product_name

order_status=[('pending','pending'),
              ('confirmed','confirmed'),
              ('cancelled','cancelled'),
              ('shipped','shipped'),
              ('out_for_delivered','out_for_delivered')
              ]

class OrderModel(models.Model):
    usr=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    pro=models.ForeignKey(ProductModel,on_delete=models.CASCADE,null=True)
    fullname=models.CharField(max_length=50,null=True)
    mobile = models.IntegerField(null=True)
    alternative_mobile = models.IntegerField(null=True)
    house_no=models.CharField(max_length=30,null=True)
    area=models.CharField(max_length=50,null=True)
    address1=models.CharField(max_length=50,null=True)
    address2=models.CharField(max_length=50,null=True)
    pincode=models.IntegerField(null=True)
    order_id=models.IntegerField(null=True,blank=True)
    payment_id=models.CharField(max_length=500,null=True,blank=True)
    payment_status=models.CharField(max_length=500,default='Not Done')
    amount=models.FloatField(null=True)
    order_status=models.CharField(max_length=50,null=True,choices=order_status)


    def __str__(self):
        return self.pro.product_name

