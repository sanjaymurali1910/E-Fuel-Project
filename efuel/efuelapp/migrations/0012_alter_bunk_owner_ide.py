# Generated by Django 3.2.12 on 2022-05-02 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('efuelapp', '0011_alter_bunk_booked_bunkowner_ide'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bunk',
            name='owner_ide',
            field=models.CharField(max_length=240, null=True),
        ),
    ]