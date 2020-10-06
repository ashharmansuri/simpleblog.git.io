# Generated by Django 3.1.1 on 2020-10-06 05:58

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0021_following'),
    ]

    operations = [
        migrations.AddField(
            model_name='following',
            name='follower',
            field=models.ManyToManyField(related_name='follower', to=settings.AUTH_USER_MODEL),
        ),
    ]
