# Generated by Django 3.2 on 2022-10-13 11:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_image_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image_url',
        ),
    ]
