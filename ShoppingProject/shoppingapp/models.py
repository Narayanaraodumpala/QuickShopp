
from django.db import models


class Categire(models.Model):
    categirie =models.CharField(max_length=30 ,null=True)

    def __str__(self):
        return self.categirie

class ProductModel(models.Model):
    product_id =models.IntegerField(null=True)
    product_name = models.CharField(max_length=100 ,null=True)
    product_price = models.FloatField(null=True)
    product_categire = models.ForeignKey(Categire ,on_delete=models.CASCADE ,null=True)
    current_status = models.CharField(max_length=15 ,null=True)
    product_for = models.CharField(max_length=20 ,null=True)
    valid_upto = models.FloatField(null=True)
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