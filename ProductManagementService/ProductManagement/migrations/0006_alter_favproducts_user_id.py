# Generated by Django 4.2.4 on 2023-08-08 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProductManagement', '0005_alter_favproducts_product_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favproducts',
            name='user_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
