# Generated by Django 3.2.8 on 2021-10-30 09:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_categories_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='Parent',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='blog.categories', verbose_name='زیر دسته'),
        ),
    ]