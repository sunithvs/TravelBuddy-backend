from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Gallery(models.Model):
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    title = models.CharField(max_length=100)
    description = models.TextField(default="")

    def __str__(self):
        return self.title


class Traveler(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Traveler')
    phone_number = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    preferred_destination = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username


class TravelAgent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='travel_agents')
    company_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    services_offered = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username


class Destination(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    dos = models.TextField()
    donts = models.TextField()
    gallery = models.ManyToManyField(Gallery, blank=True)

    def __str__(self):
        return self.title

    def get_dos(self):
        return self.dos.split(',')

    def get_donts(self):
        return self.donts.split(',')


class Blog(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(default="lorem ipsum")
    content = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    topics = models.CharField(max_length=100, choices=(
        ('Travel', 'Travel'), ('Food', 'Food'), ('Culture', 'Culture'), ('History', 'History'), ('Nature', 'Nature'),
        ('Other', 'Other')))
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name='blogs', null=True, blank=True)

    def __str__(self):
        return self.title


class Hotel(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    rating = models.FloatField()
    price_range = models.CharField(max_length=100)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name='hotels')
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.name


class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    location = models.CharField(max_length=100)
    travel_agent = models.ForeignKey(TravelAgent, on_delete=models.CASCADE, related_name='events')
    gallery = models.ManyToManyField(Gallery, blank=True)
    def __str__(self):
        return self.title


class Review(models.Model):
    rating = models.IntegerField()
    content = models.TextField()
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name='reviews')
    traveler = models.ForeignKey(Traveler, on_delete=models.CASCADE, related_name='reviews')

    def __str__(self):
        return self.content


class Booking(models.Model):
    traveler = models.ForeignKey(Traveler, on_delete=models.CASCADE, related_name='bookings')
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='bookings')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='bookings')
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    total_price = models.FloatField()

    def __str__(self):
        return self.traveler.user.username + ' ' + self.hotel.name + ' ' + self.event.title


class Package(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    price = models.FloatField()
    travel_agent = models.ForeignKey(TravelAgent, on_delete=models.CASCADE, related_name='packages')
    destinations = models.ManyToManyField(Destination, related_name='packages', blank=True)

    def __str__(self):
        return self.title
