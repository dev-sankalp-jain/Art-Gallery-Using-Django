from django.db import models
import os
from django.contrib.auth import get_user_model
from datetime import datetime
# Create your models here.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

User = get_user_model()


# Artist
class Artist(models.Model):

    artist_name = models.CharField(max_length=300)
    speciality = models.CharField(max_length=300)

# Art


class Art(models.Model):

    art_name = models.CharField(max_length=50, null=False, blank=False)
    art_artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=os.path.join(BASE_DIR, "media"))
    price = models.FloatField(null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    instock = models.BooleanField(null = False,blank=False, default=True)


# TAGs
class Category(models.Model):

    tag = models.CharField(max_length=300, null=False)
    artid = models.ForeignKey(Art, on_delete=models.CASCADE)

# Cart Table

class MyCart(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    art_id = models.ForeignKey(Art, on_delete=models.CASCADE)
    added_date = models.DateTimeField(default=datetime.now())


# Order Table


class MyOrder(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    art_id = models.ForeignKey(Art, on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.now())
    

# Employee


class Employee(models.Model):

    emp_name = models.CharField(max_length=50, null=False, blank=False)
    phone = models.CharField(max_length=13, null=False, blank=False, unique=True)
    email = models.EmailField(null=False, blank=False, unique=True)
    password = models.CharField(max_length=20, null=False, blank=False, unique=True)
    post = models.CharField(max_length=20, null=False, blank=False)
    address = models.TextField(null=False, blank=False)
    salary = models.FloatField(null=False, blank=False)
