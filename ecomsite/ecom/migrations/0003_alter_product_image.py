# Generated by Django 4.0.10 on 2024-05-18 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0002_category_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='https://www.staticwhich.co.uk/static/images/products/no-image/no-image-available.png', upload_to='products/'),
        ),
    ]