from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)  # Add a description field

    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200, default="Unknown")  # Provide a default value
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name



class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()  # You already have the description field
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    date = models.DateTimeField()
    organizer = models.CharField(max_length=100)

    def __str__(self):
        return self.title
