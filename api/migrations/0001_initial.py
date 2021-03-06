# Generated by Django 3.0.3 on 2020-02-21 08:01

from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Excursion',
            fields=[
                ('id', models.CharField(max_length=36, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=225)),
                ('detailPageName', models.CharField(max_length=225)),
                ('portID', models.CharField(max_length=5)),
                ('type', models.CharField(max_length=36)),
                ('typology', django_mysql.models.ListCharField(models.CharField(max_length=10), max_length=66, size=6)),
                ('activityLevel', models.CharField(max_length=225)),
                ('collectionType', models.CharField(max_length=225)),
                ('duration', models.CharField(max_length=225)),
                ('language', django_mysql.models.ListCharField(models.CharField(max_length=10), max_length=66, size=6)),
                ('priceLevel', models.IntegerField()),
                ('currency', models.CharField(max_length=8)),
                ('mealInfo', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=36)),
                ('shortDescription', models.TextField()),
                ('longDescription', models.TextField()),
                ('externalContent', models.BooleanField()),
                ('minimumAge', models.CharField(max_length=25)),
                ('wheelChairAccessible', models.BooleanField()),
                ('featured', models.BooleanField()),
            ],
        ),
    ]
