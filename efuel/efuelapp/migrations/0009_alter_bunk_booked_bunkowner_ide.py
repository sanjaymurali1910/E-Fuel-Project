# Generated by Django 3.2.12 on 2022-05-01 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('efuelapp', '0008_alter_bunk_booked_bunkowner_ide'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bunk_booked',
            name='bunkowner_ide',
            field=models.IntegerField(blank=True, default='0', null=True),
        ),
    ]
