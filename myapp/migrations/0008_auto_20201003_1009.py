# Generated by Django 3.1.1 on 2020-10-03 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_auto_20201002_2320'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profession',
            field=models.CharField(blank=True, max_length=90),
        ),
        migrations.AddField(
            model_name='profile',
            name='qualification',
            field=models.CharField(blank=True, max_length=90),
        ),
    ]