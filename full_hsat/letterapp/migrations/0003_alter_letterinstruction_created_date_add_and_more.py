# Generated by Django 4.2.5 on 2023-10-30 05:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('letterapp', '0002_alter_letterinstruction_created_date_add_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='letterinstruction',
            name='created_date_add',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 29, 5, 26, 43, 239696, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='lettersummons',
            name='created_date_add',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 4, 5, 26, 43, 240157, tzinfo=datetime.timezone.utc)),
        ),
    ]
