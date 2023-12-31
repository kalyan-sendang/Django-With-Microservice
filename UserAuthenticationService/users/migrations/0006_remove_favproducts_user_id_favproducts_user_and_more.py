# Generated by Django 4.2.4 on 2023-08-07 10:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_remove_user_fav_products'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favproducts',
            name='user_id',
        ),
        migrations.AddField(
            model_name='favproducts',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='favproducts',
            name='product_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
