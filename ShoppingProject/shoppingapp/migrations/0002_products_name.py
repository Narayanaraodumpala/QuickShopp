# Generated by Django 3.0 on 2020-11-10 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoppingapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='name',
            field=models.CharField(max_length=60, null=True),
        ),
    ]
