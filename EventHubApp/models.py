from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200, default="Unknown")
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name



class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    date = models.DateTimeField()
    organizer = models.CharField(max_length=100)
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    def __str__(self):
        return self.title
