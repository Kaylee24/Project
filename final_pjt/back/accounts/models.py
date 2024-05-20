from django.db import models
from django.contrib.auth.models import AbstractUser
from countries.models import Country

# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    age = models.IntegerField(default=4)
    email = models.CharField(max_length=50)
    visited = models.ManyToManyField(Country, related_name='visited_users', blank=True)
    interested = models.ManyToManyField(Country, related_name='interested_users', blank=True)

    def __str__(self):
        return self.username

from allauth.account.adapter import DefaultAccountAdapter
class CustomAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=True):
        from allauth.account.utils import user_email, user_field, user_username
        data = form.cleaned_data
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        email = data.get("email")
        username = data.get("username")
        name = data.get("name")
        gender = data.get("gender")
        age = data.get("age")
        user_email(user, email)
        user_username(user, username)
        if first_name:
            user_field(user, "first_name", first_name)
        if last_name:
            user_field(user, "last_name", last_name)
        if name:
            user_field(user, "name", name)
        if gender:
            user_field(user, "gender", gender)
        if age:
            user_field(user, "age", age)
        if "password1" in data:
            user.set_password(data["password1"])
        else:
            user.set_unusable_password()
        self.populate_username(request, user)
        if commit:
            user.save()
        return user