# Generated by Django 3.1.1 on 2020-10-04 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0016_blogcomment_reply'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='download.png', upload_to='profileimg'),
        ),
    ]
