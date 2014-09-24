from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Venue(models.Model):
    name = models.CharField(max_length=30)
    details = models.TextField()
    address1 = models.CharField(max_length=30)
    address2 = models.CharField(max_length=30)
    address3 = models.CharField(max_length=30, blank = True)
    town = models.CharField(max_length=30)
    postcode = models.CharField(max_length=10)
    website = models.URLField()
    image_url = models.URLField()
    map_id = models.FloatField()
    phone = models.IntegerField(max_length=11)
    total_seats = models.IntegerField()
    featured = models.BooleanField()
    def __str__(self):
        return self.name
class Event(models.Model):
    name = models.CharField(max_length=30)
    details = models.TextField(blank = True)
    date = models.DateTimeField()
    finish_time = models.TimeField()
    total_seats = models.IntegerField()
    seats_avalable = models.IntegerField()
    venue = models.ForeignKey(Venue)
    website = models.URLField(blank = True)
    image_url = models.URLField(blank = True)
    featured = models.BooleanField()
    def __str__(self):
        return self.name

    def seats_free(self):
        return self.total_seats - self.seats_taken


class Price(models.Model):
    name = models.CharField(max_length=30)
    event = models.ForeignKey(Event)
    notes = models.CharField(max_length=100, blank = True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    def __str__(self):
        return (self.event.name +" - " + self.name)

class Ticket(models.Model):
    tOwner = models.OneToOneField(User)
    tEvent = models.OneToOneField(Event)
    tPrice = models.OneToOneField(Price)
    def __str__(self):
        return str(self.pk)



class Person(models.Model):
    user = models.OneToOneField(User)
    tickets = models.ManyToManyField(Ticket)
    DOB = models.DateField()
    def __str__(self):
        return str(self.user.Username)

    @property
    def age(self):
        from datetime import date
        if (date.today() - self.DOB.replace(year=date.today().year)).days >= 0:
            age = years
        else:
            age = years - 1
        return age  

