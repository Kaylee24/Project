from django.db import models
from django.contrib.auth.models import AbstractUser
from countries.models import Country

# Create your models here.
class User(AbstractUser):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=50, choices=GENDER_CHOICES)
    age = models.IntegerField(default=4)
    visited = models.ManyToManyField(Country, related_name='visited_users')
    interested = models.ManyToManyField(Country, related_name='interested_users')
    