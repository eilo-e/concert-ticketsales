# Generated by Django 4.2.11 on 2024-05-31 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketsale', '0002_timeconert_status_alter_profile_nationalcode_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeconert',
            name='status',
            field=models.IntegerField(choices=[(1, 'فروش بلیط'), (2, 'پایان'), (3, 'کنسل'), (4, 'کامل فروخته شده')], default='start'),
        ),
    ]