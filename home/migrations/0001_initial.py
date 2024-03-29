# Generated by Django 2.2.4 on 2019-08-08 11:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity_name_en', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('activity_name_ar', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('activity_description_en', models.TextField(blank=True, default='', null=True)),
                ('activity_description_ar', models.TextField(blank=True, default='', null=True)),
                ('activity_date', models.DateField(blank=True, default=datetime.date.today, null=True, verbose_name='Date')),
                ('activity_image', models.TextField(blank=True, default='', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mem_uid', models.CharField(blank=True, default='', max_length=9, null=True)),
                ('mem_first_name_en', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('mem_first_name_ar', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('mem_mid_name_en', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('mem_mid_name_ar', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('mem_last_name_en', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('mem_last_name_ar', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('mem_major_en', models.CharField(blank=True, default='', max_length=30, null=True)),
                ('mem_major_ar', models.CharField(blank=True, default='', max_length=30, null=True)),
                ('mem_rank_en', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('mem_rank_ar', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('mem_points', models.IntegerField(blank=True, default=0, null=True)),
                ('mem_phone', models.CharField(blank=True, default='', max_length=9, null=True)),
                ('mem_image_url', models.TextField(blank=True, default='', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('msg_sender_name', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('msg_sender_email', models.EmailField(blank=True, default='', max_length=70, null=True)),
                ('msg_content', models.TextField(blank=True, default='', null=True)),
                ('msg_date', models.DateField(blank=True, default=datetime.date.today, null=True, verbose_name='Date')),
            ],
        ),
    ]
