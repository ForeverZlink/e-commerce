# Generated by Django 3.1.7 on 2021-10-15 00:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Imagem_Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_image', models.CharField(max_length=100, unique=True)),
                ('imagem_of_product', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Mark_Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_mark', models.CharField(max_length=100)),
                ('description_of_mark', models.TextField()),
                ('date_of_creation', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Type_of_Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_product', models.CharField(max_length=100)),
                ('public_target', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('price', models.FloatField()),
                ('descripition', models.TextField()),
                ('imagem_product', models.ManyToManyField(to='products.Imagem_Product')),
                ('mark_of_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.mark_product')),
                ('type_of_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.type_of_product')),
            ],
        ),
    ]
