# Generated by Django 3.2.5 on 2021-07-11 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0007_alter_post_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippts',
            field=models.CharField(default='', max_length=255),
        ),
    ]
