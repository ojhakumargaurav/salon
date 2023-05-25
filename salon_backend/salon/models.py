from django.db import models
from django.contrib.auth.models import User


class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.TextField()

    def __str__(self):
        return self.name


class Appointment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return f"{self.name} - {self.service.name}"


class SubscriptionDetails(models.Model):
    Name = models.TextField()
    description = models.TextField()
    discount_percent = models.DecimalField(max_digits=2, decimal_places=2)


class BusinessUser(User):
    subscription_type = models.ForeignKey(SubscriptionDetails, on_delete=models.CASCADE)
