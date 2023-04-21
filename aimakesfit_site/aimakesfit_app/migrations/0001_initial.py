# Generated by Django 4.1.7 on 2023-04-18 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100)),
                ('fitness_goal', models.CharField(max_length=100)),
                ('height', models.FloatField()),
                ('weight', models.FloatField()),
                ('gender', models.CharField(max_length=100)),
                ('medical_conditions', models.CharField(max_length=300)),
                ('activity_level', models.CharField(max_length=100)),
                ('dietary_preference', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('location', models.CharField(max_length=100)),
                ('cooking_time', models.CharField(max_length=100)),
                ('budget', models.CharField(max_length=100)),
                ('allergies', models.CharField(max_length=300)),
            ],
        ),
    ]