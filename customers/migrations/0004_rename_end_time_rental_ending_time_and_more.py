# Generated by Django 5.1.2 on 2024-10-28 09:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0003_location'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rental',
            old_name='end_time',
            new_name='ending_time',
        ),
        migrations.RenameField(
            model_name='rental',
            old_name='id',
            new_name='rent_id',
        ),
        migrations.RenameField(
            model_name='rental',
            old_name='start_time',
            new_name='starting_time',
        ),
        migrations.RenameField(
            model_name='vehicle',
            old_name='battery_level',
            new_name='charging_level',
        ),
        migrations.RenameField(
            model_name='vehicle',
            old_name='id',
            new_name='vehicle_id',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='is_working',
        ),
        migrations.AddField(
            model_name='rental',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='customers.location'),
        ),
        migrations.AddField(
            model_name='rental',
            name='total_hours',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='charge_per_hour',
            field=models.DecimalField(decimal_places=2, default=10.0, max_digits=6),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='miles_per_percent_charge',
            field=models.DecimalField(decimal_places=2, default=0.5, max_digits=5),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='status',
            field=models.CharField(choices=[('available', 'Available'), ('unavailable', 'Unavailable'), ('maintenance', 'Maintenance'), ('out_of_service', 'Out of Service')], default='available', max_length=20),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='vehicle_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.location'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='vehicle_type',
            field=models.CharField(choices=[('bike', 'Bike'), ('scooter', 'Scooter')], max_length=10),
        ),
    ]
