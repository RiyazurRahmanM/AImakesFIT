from django.db import models

# Create your models here.
class Users(models.Model):
    email = models.CharField(max_length=100)
    fitness_goal = models.CharField(max_length=100)
    height = models.FloatField()
    weight = models.FloatField()
    gender = models.CharField(max_length=100)
    medical_conditions = models.CharField(max_length=300)
    activity_level = models.CharField(max_length=100)
    dietary_preference = models.CharField(max_length=100)
    age = models.IntegerField()
    location = models.CharField(max_length=100)
    cooking_time = models.CharField(max_length=100)
    budget =models.CharField(max_length=100)
    allergies = models.CharField(max_length=300)
    