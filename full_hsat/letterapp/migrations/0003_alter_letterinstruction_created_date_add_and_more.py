# Generated by Django 4.2.6 on 2023-11-02 08:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("letterapp", "0002_alter_letterinstruction_created_date_add_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="letterinstruction",
            name="created_date_add",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 12, 2, 8, 19, 58, 317964, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="lettersummons",
            name="created_date_add",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 11, 7, 8, 19, 58, 318764, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
