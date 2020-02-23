from django.db import models
from django_mysql.models import ListCharField

# Create your models here.
class Excursion(models.Model):
    id = models.CharField(max_length=36, primary_key=True)
    name = models.CharField(max_length=225)
    detailPageName = models.CharField(max_length=225)
    portID = models.CharField(max_length=5)
    type = models.CharField(max_length=36)
    typology = ListCharField( base_field=models.CharField(max_length=10),
        size=6,
        max_length=(6 * 11))
    activityLevel = models.CharField(max_length=225)
    collectionType = models.CharField(max_length=225)
    duration = models.CharField(max_length=225)
    language = ListCharField( base_field=models.CharField(max_length=10),
        size=6,
        max_length=(6 * 11))
    priceLevel = models.IntegerField()
    currency = models.CharField(max_length=8)
    mealInfo = models.CharField(max_length=255)
    status = models.CharField(max_length=36)
    shortDescription = models.TextField()
    longDescription = models.TextField()
    externalContent = models.BooleanField()
    minimumAge = models.CharField(max_length=25)
    wheelChairAccessible = models.BooleanField()
    featured = models.BooleanField()

       
       