# Generated by Django 3.1.1 on 2020-10-03 12:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_remove_blogcomment_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogcomment',
            name='reply',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='myapp.blogcomment'),
        ),
    ]
