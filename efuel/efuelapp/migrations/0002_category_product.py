# Generated by Django 3.2.12 on 2022-04-27 06:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('efuelapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=225)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=40)),
                ('product_image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('price', models.PositiveIntegerField()),
                ('description', models.CharField(max_length=40)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='efuelapp.category')),
            ],
        ),
    ]
