# Generated by Django 3.1.1 on 2020-10-05 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0019_auto_20201004_2133'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='follower',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='following',
            field=models.IntegerField(default=0),
        ),
    ]
