# Generated by Django 2.1.5 on 2019-04-28 04:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('furniapp', '0009_auto_20190428_1027'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='home',
            name='category',
        ),
    ]
