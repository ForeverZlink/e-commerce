# Generated by Django 3.2.8 on 2021-12-15 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='delivered',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='orders',
            name='status',
            field=models.CharField(default='', max_length=200),
        ),
    ]
