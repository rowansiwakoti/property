# Generated by Django 3.2 on 2023-02-13 22:49

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('realtors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=21)),
            ],
        ),
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('property_type', models.CharField(choices=[('apartments', 'Apartments'), ('penthouses', 'Penthouses'), ('houses', 'Houses'), ('villas', 'Villas'), ('bungalows', 'Bungalows'), ('lands', 'Lands'), ('flats', 'Flats'), ('shops', 'Shops')], max_length=17)),
                ('purpose', models.CharField(choices=[('sell', 'Sell'), ('rent', 'Rent')], max_length=4)),
                ('price', models.IntegerField()),
                ('furnish_type', models.CharField(choices=[('unfurnished', 'Unfurnished'), ('semi_furnished', 'Semi Furnished'), ('fully_furnished', 'Fully Furnished')], default='Furnished', max_length=15)),
                ('area', models.CharField(blank=True, max_length=50)),
                ('bedrooms', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)])),
                ('bathrooms', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)])),
                ('living', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], default=0)),
                ('kitchen', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], default=0)),
                ('floor', models.IntegerField(default=1)),
                ('road_size', models.IntegerField(default=20)),
                ('road_condition', models.CharField(choices=[('kachchi', 'Kachchi'), ('gravel', 'Gravel'), ('pitch', 'Pitch')], default='Kachchi', max_length=20)),
                ('facing_direction', models.CharField(choices=[('east', 'East'), ('west', 'West'), ('north', 'North'), ('south', 'South'), ('north_east', 'North East'), ('north_west', 'North West'), ('south_east', 'South East'), ('south_west', 'South West')], default='East', max_length=40)),
                ('available_from', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('built_year', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('city', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, max_length=500)),
                ('photo_main', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('photo_1', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_2', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_3', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_4', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_5', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_6', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_7', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_8', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('is_published', models.BooleanField(default=True)),
                ('list_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('district', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='listings.district')),
                ('province', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='listings.province')),
                ('realtor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='realtors.realtor')),
            ],
        ),
        migrations.AddField(
            model_name='district',
            name='province',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='listings.province'),
        ),
    ]
