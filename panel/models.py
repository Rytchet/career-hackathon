from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=200)
    completed = models.BooleanField()
    points = models.IntegerField()


class Event(models.Model):
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=200)
    date = models.DateTimeField()
    points = models.IntegerField()

class Points(models.Model):
    points = models.IntegerField()
