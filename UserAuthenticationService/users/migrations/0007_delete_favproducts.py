# Generated by Django 4.0.4 on 2023-08-08 11:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_remove_favproducts_user_id_favproducts_user_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='FavProducts',
        ),
    ]