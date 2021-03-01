from django.db import models

# Create your models here.
class Weather(models.Model):
            id =  models.AutoField(primary_key=True, unique=True)
            city = models.CharField(max_length=200)
            country_code = models.CharField(max_length=200)
            coordinate = models.CharField(max_length=200)
            temp = models.CharField(max_length=200)
            pressure = models.CharField(max_length=200)
            humidity = models.CharField(max_length=200)
            description = models.CharField(max_length=200)
            humidity = models.CharField(max_length=200)

