# Generated by Django 5.0.7 on 2024-07-13 02:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_comments_created_date_alter_post_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 13, 2, 25, 5, 574058, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 13, 2, 25, 5, 574058, tzinfo=datetime.timezone.utc)),
        ),
    ]
