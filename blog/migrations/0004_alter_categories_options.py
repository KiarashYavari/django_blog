# Generated by Django 3.2.8 on 2021-10-30 07:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20211030_1037'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categories',
            options={'ordering': ['Parent__id', 'Position'], 'verbose_name': 'دسته بندی', 'verbose_name_plural': 'دسته بندی ها'},
        ),
    ]
