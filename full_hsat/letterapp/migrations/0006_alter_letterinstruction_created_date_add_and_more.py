# Generated by Django 4.2.6 on 2023-10-30 05:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('letterapp', '0005_alter_letterinstruction_created_date_add_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='letterinstruction',
            name='created_date_add',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 29, 5, 40, 27, 482616, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='lettersummons',
            name='created_date_add',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 4, 5, 40, 27, 483079, tzinfo=datetime.timezone.utc)),
        ),
    ]
