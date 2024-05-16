from django.db import models
from django.conf import settings

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=50)
    burger = models.FloatField()
    coffee = models.FloatField()
    area = models.CharField(max_length=50)

class Exchange(models.Model):
    country_e = models.ForeignKey(Country, on_delete=models.CASCADE)
    code = models.CharField(max_length=50)
    rate = models.FloatField()
    graph = models.ImageField(blank=True)

class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Travel(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    country_t = models.ManyToManyField(Country, related_name='travel')
    budget = models.IntegerField()
    period = models.IntegerField()