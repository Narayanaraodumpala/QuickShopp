# Generated by Django 3.0 on 2020-11-19 17:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shoppingapp', '0012_remove_addtocartmodel_pro'),
    ]

    operations = [
        migrations.AddField(
            model_name='addtocartmodel',
            name='categire',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shoppingapp.Categire'),
        ),
        migrations.AddField(
            model_name='addtocartmodel',
            name='image',
            field=models.ImageField(null=True, upload_to='cart_images/'),
        ),
        migrations.AddField(
            model_name='addtocartmodel',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='addtocartmodel',
            name='p_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='addtocartmodel',
            name='price',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='addtocartmodel',
            name='product_for',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='addtocartmodel',
            name='size',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='addtocartmodel',
            name='valid_upto',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
