# Generated by Django 5.0.7 on 2024-09-20 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='capital',
            name='Capial_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='country',
            name='Country_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
