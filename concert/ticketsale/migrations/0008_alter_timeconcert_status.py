# Generated by Django 4.2.11 on 2024-06-05 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketsale', '0007_rename_timeconert_timeconcert'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeconcert',
            name='status',
            field=models.IntegerField(choices=[(1, 'فروش بلیط'), (2, 'پایان'), (3, 'کنسل'), (4, 'کامل فروخته شده')]),
        ),
    ]