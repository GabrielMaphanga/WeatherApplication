# Generated by Django 3.1.7 on 2021-02-28 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=200)),
                ('country_code', models.CharField(max_length=200)),
                ('coordinate', models.CharField(max_length=200)),
                ('temp', models.CharField(max_length=200)),
                ('pressure', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('humidity', models.CharField(max_length=200)),
            ],
        ),
    ]
