# Generated by Django 4.1.7 on 2023-04-08 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BangloreJobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=20)),
                ('positions', models.IntegerField()),
                ('address', models.CharField(max_length=20)),
                ('mail', models.EmailField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='HydJobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=20)),
                ('positions', models.IntegerField()),
                ('address', models.CharField(max_length=20)),
                ('mail', models.EmailField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='PuneJobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=20)),
                ('positions', models.IntegerField()),
                ('address', models.CharField(max_length=20)),
                ('mail', models.EmailField(max_length=20)),
            ],
        ),
    ]
