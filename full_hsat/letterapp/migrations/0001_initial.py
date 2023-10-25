# Generated by Django 4.2.5 on 2023-10-22 09:47

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='LetterSummons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(default=datetime.datetime(2023, 10, 22, 9, 47, 4, 713269, tzinfo=datetime.timezone.utc), editable=False)),
                ('update_date', models.DateTimeField(default=datetime.datetime(2023, 10, 22, 9, 47, 4, 713285, tzinfo=datetime.timezone.utc))),
                ('letter_name', models.CharField(max_length=50)),
                ('litter_number', models.CharField(max_length=15, unique=True)),
                ('adress', models.CharField(max_length=100)),
                ('street', models.CharField(max_length=100)),
                ('company_name', models.CharField(max_length=150)),
                ('stir_number', models.PositiveBigIntegerField(default=0)),
                ('phone_number', models.CharField(max_length=13)),
                ('report_name', models.CharField(max_length=100)),
                ('report_date', models.DateTimeField()),
                ('created_date_add', models.DateTimeField(default=datetime.datetime(2023, 10, 27, 9, 47, 4, 713913, tzinfo=datetime.timezone.utc))),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LetterInstruction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(default=datetime.datetime(2023, 10, 22, 9, 47, 4, 713269, tzinfo=datetime.timezone.utc), editable=False)),
                ('update_date', models.DateTimeField(default=datetime.datetime(2023, 10, 22, 9, 47, 4, 713285, tzinfo=datetime.timezone.utc))),
                ('letter_name', models.CharField(max_length=50)),
                ('litter_number', models.CharField(max_length=15, unique=True)),
                ('adress', models.CharField(max_length=100)),
                ('street', models.CharField(max_length=100)),
                ('company_name', models.CharField(max_length=150)),
                ('stir_number', models.PositiveBigIntegerField(default=0)),
                ('phone_number', models.CharField(max_length=13)),
                ('report_name', models.CharField(max_length=100)),
                ('report_date', models.DateTimeField()),
                ('created_date_add', models.DateTimeField(default=datetime.datetime(2023, 11, 21, 9, 47, 4, 713476, tzinfo=datetime.timezone.utc))),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LetterCourt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(default=datetime.datetime(2023, 10, 22, 9, 47, 4, 713269, tzinfo=datetime.timezone.utc), editable=False)),
                ('update_date', models.DateTimeField(default=datetime.datetime(2023, 10, 22, 9, 47, 4, 713285, tzinfo=datetime.timezone.utc))),
                ('letter_name', models.CharField(max_length=50)),
                ('litter_number', models.CharField(max_length=15, unique=True)),
                ('company_name', models.CharField(max_length=150)),
                ('ptsh', models.CharField(max_length=15)),
                ('stir_number', models.PositiveBigIntegerField(blank=True, default=0, null=True)),
                ('report_name', models.CharField(max_length=100)),
                ('report_date', models.DateTimeField()),
                ('company_own', models.CharField(max_length=50)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]