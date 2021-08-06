# Generated by Django 3.2.5 on 2021-08-06 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True)),
                ('scheduled', models.DateTimeField()),
                ('appointment_end', models.CharField(blank=True, max_length=50, null=True)),
                ('created_date_time', models.DateTimeField(auto_now_add=True)),
                ('day', models.CharField(blank=True, max_length=50, null=True)),
                ('status', models.CharField(blank=True, choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Cancelled', 'Cancelled'), ('Declined', 'Declined'), ('Completed', 'Completed')], max_length=100, null=True)),
                ('payment_status', models.BooleanField(default=False)),
            ],
        ),
    ]
