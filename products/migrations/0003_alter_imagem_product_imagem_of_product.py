# Generated by Django 3.2.8 on 2021-10-18 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagem_product',
            name='imagem_of_product',
            field=models.ImageField(upload_to='media'),
        ),
    ]