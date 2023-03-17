from django.db import models


# Create your models here.

class Attractions(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    image_url = models.CharField(max_length=100)
    rating = models.IntegerField()
    price = models.IntegerField()
    duration = models.IntegerField()
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class DosDonts(models.Model):
    attraction = models.ForeignKey(Attractions, on_delete=models.CASCADE, related_name='dos_donts')
    dos = models.CharField(max_length=100)
    donts = models.CharField(max_length=100)

    def __str__(self):
        return self.dos


class NearbyHotels(models.Model):
    attraction = models.ForeignKey(Attractions, on_delete=models.CASCADE, related_name='nearby_hotels')
    hotel_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    image_url = models.CharField(max_length=100)
    rating = models.IntegerField()
    price = models.IntegerField()
    distance = models.IntegerField()

    def __str__(self):
        return self.hotel_name


class ThingsToExplore(models.Model):
    attraction = models.ForeignKey(Attractions, on_delete=models.CASCADE, related_name='things_to_explore')
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    image_url = models.CharField(max_length=100)
    rating = models.IntegerField()
    price = models.IntegerField()
    duration = models.IntegerField()

    def __str__(self):
        return self.name
