# Generated by Django 3.1.5 on 2021-02-11 13:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce_app', '0004_auto_20210211_1355'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='stock',
            new_name='max_quantity',
        ),
    ]