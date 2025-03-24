from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Login(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_owner = models.BooleanField(default=False)

class customer(models.Model):
    customer_data = models.ForeignKey("Login",on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    phone_no = models.CharField(max_length=15)

class owner(models.Model):
    owner_data = models.ForeignKey("Login", on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone_no = models.CharField(max_length=15)


class book_now(models.Model):
    vehicle = models.ForeignKey("vehicle", on_delete=models.DO_NOTHING)
    customer = models.ForeignKey("customer", on_delete=models.DO_NOTHING)
    start_date = models.DateField()
    end_date = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.IntegerField(default=0)

class vehicle(models.Model):
    owner = models.ForeignKey("owner",on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    vehicle_type = models.CharField(max_length=20, choices=[('car', 'Car'), ('bike', 'Bike')])
    description = models.CharField(max_length=400)
    price_per_day = models.CharField(max_length=8)
    image = models.FileField(upload_to="images/")
    available = models.BooleanField(default=True)

class pay(models.Model):
    book = models.ForeignKey("book_now",on_delete=models.CASCADE)
    card_no = models.CharField(max_length=16)
    expiry_date = models.DateField()