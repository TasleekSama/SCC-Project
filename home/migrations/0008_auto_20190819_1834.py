# Generated by Django 2.2.4 on 2019-08-19 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20190819_1825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='activity_image',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='activity',
            name='day_five',
            field=models.CharField(blank=True, default=' ', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='activity',
            name='day_four',
            field=models.CharField(blank=True, default=' ', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='activity',
            name='day_one',
            field=models.CharField(blank=True, default='-', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='activity',
            name='day_three',
            field=models.CharField(blank=True, default='-', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='activity',
            name='day_two',
            field=models.CharField(blank=True, default='-', max_length=200, null=True),
        ),
    ]
