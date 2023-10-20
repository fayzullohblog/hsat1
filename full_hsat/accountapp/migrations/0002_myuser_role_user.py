# Generated by Django 4.2.5 on 2023-10-17 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='role_user',
            field=models.CharField(choices=[('admin', 'Admin'), ('boss', 'Boss'), ('staff', 'Staff')], default='staff', max_length=5),
        ),
    ]