# Generated by Django 3.1.5 on 2021-02-09 16:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce_app', '0002_auto_20210209_1801'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='updated',
        ),
    ]