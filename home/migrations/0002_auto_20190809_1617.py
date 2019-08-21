# Generated by Django 2.2.4 on 2019-08-09 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='mem_points',
            new_name='mem_current_order_in_names',
        ),
        migrations.RemoveField(
            model_name='member',
            name='mem_image_url',
        ),
        migrations.RemoveField(
            model_name='member',
            name='mem_major_ar',
        ),
        migrations.RemoveField(
            model_name='member',
            name='mem_major_en',
        ),
        migrations.RemoveField(
            model_name='member',
            name='mem_mid_name_ar',
        ),
        migrations.RemoveField(
            model_name='member',
            name='mem_mid_name_en',
        ),
        migrations.RemoveField(
            model_name='member',
            name='mem_phone',
        ),
        migrations.RemoveField(
            model_name='member',
            name='mem_rank_ar',
        ),
        migrations.RemoveField(
            model_name='member',
            name='mem_rank_en',
        ),
        migrations.AddField(
            model_name='member',
            name='mem_current_points',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='mem_last_order_in_names',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='mem_last_points',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
