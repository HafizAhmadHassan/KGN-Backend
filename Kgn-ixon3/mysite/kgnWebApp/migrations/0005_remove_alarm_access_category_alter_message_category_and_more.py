# Generated by Django 5.0.2 on 2024-04-04 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kgnWebApp', '0004_remove_alarm_severity_remove_alarm_threshold_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alarm',
            name='access_category',
        ),
        migrations.AlterField(
            model_name='message',
            name='category',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='card_Number',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='category',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_Number',
            field=models.BigIntegerField(default=0),
        ),
    ]