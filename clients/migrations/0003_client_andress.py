# Generated by Django 3.2.8 on 2022-02-17 00:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0002_client_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='andress',
            field=models.OneToOneField(blank=True, default=0, on_delete=django.db.models.deletion.DO_NOTHING, to='clients.andress'),
            preserve_default=False,
        ),
    ]