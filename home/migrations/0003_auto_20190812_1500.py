# Generated by Django 2.2.4 on 2019-08-12 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20190809_1617'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='mem_full_name_ar',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='mem_full_name_en',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
    ]
