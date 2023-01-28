# Generated by Django 2.2.27 on 2023-01-28 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0005_auto_20230128_1346'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='property_type',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='purpose',
        ),
        migrations.AddField(
            model_name='listing',
            name='city',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='listing',
            name='garage',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='listing',
            name='lot_size',
            field=models.DecimalField(decimal_places=1, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='listing',
            name='state',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='listing',
            name='zipcode',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
