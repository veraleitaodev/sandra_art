# Generated by Django 3.1.5 on 2021-01-24 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_sold'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='dimension',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]
