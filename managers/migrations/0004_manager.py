# Generated by Django 5.1.2 on 2024-10-19 15:06

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managers', '0003_delete_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(default='loc', max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('mobile_number', models.CharField(default='', max_length=15, unique=True)),
                ('password', models.CharField(default='', max_length=128)),
                ('balance', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('joined_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
