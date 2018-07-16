from django.db import models

# Create your models here.


class Beer(models.Model):
    name = models.CharField(max_length=100, blank=False)
    brewery = models.CharField(max_length=100, blank=True)
    beer_style = models.CharField(max_length=80, blank=True)
    price = models.CharField(max_length=80, blank=True)
    description = models.TextField()


class Brewery(models.Model):
    name = models.CharField(max_length=100, blank=False)
    brewery = models.CharField(max_length=100, blank=True)
    price = models.CharField(max_length=80, blank=True)
    description = models.TextField()
    street_number = models.CharField(max_length=80, blank=True)
    street_name = models.CharField(max_length=80, blank=True)
    postal_code = models.CharField(max_length=80, blank=True)
    prov_state = models.CharField(max_length=80, blank=True)
    country = models.CharField(max_length=80, blank=True)


class BeerStyle(models.Model):
    name = models.CharField(max_length=100, blank=False)
    description = models.TextField()
