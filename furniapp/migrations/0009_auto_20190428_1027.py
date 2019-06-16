# Generated by Django 2.1.5 on 2019-04-28 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('furniapp', '0008_auto_20190428_0952'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='fur_name',
        ),
        migrations.AddField(
            model_name='category',
            name='name',
            field=models.CharField(db_index=True, default='Chair', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default='1', max_length=200, unique=True),
            preserve_default=False,
        ),
    ]
