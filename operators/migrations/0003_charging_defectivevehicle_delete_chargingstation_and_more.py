# Generated by Django 5.1.2 on 2024-10-28 09:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0004_rename_end_time_rental_ending_time_and_more'),
        ('operators', '0002_operator'),
    ]

    operations = [
        migrations.CreateModel(
            name='Charging',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('charge_level', models.IntegerField()),
                ('status', models.CharField(choices=[('nil', 'Nil'), ('charging', 'Charging'), ('charged', 'Charged'), ('low_battery', 'Low Battery')], default='low_battery', max_length=20)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.location')),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.vehicle')),
            ],
        ),
        migrations.CreateModel(
            name='DefectiveVehicle',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('defect_description', models.TextField()),
                ('status', models.CharField(choices=[('reported', 'Reported'), ('in_repair', 'In Repair'), ('repaired', 'Repaired'), ('not_repairable', 'Not Repairable')], default='reported', max_length=20)),
                ('reported_date', models.DateTimeField(auto_now_add=True)),
                ('repair_notes', models.TextField(blank=True)),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.vehicle')),
            ],
        ),
        migrations.DeleteModel(
            name='ChargingStation',
        ),
        migrations.RemoveField(
            model_name='relocation',
            name='vehicle',
        ),
        migrations.RemoveField(
            model_name='operator',
            name='balance',
        ),
        migrations.AlterField(
            model_name='operator',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.location'),
        ),
        migrations.DeleteModel(
            name='Maintenance',
        ),
        migrations.DeleteModel(
            name='Relocation',
        ),
    ]
