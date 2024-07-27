from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.db.models import Manager


class Retreat(models.Model):
    objects: Manager = models.Manager()
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=100)
    price = models.FloatField()
    type = models.CharField(max_length=50)
    condition = models.CharField(max_length=50)
    image = models.URLField(max_length=200)
    tag = ArrayField(models.CharField(max_length=50))
    duration = models.IntegerField()


class Booking(models.Model):
    objects: Manager = models.Manager()
    user_id = models.IntegerField()
    user_name = models.CharField(max_length=100)
    user_email = models.EmailField()
    user_phone = models.CharField(max_length=20)
    retreat = models.ForeignKey(Retreat, on_delete=models.CASCADE)
    retreat_title = models.CharField(max_length=100)
    retreat_location = models.CharField(max_length=100)
    retreat_price = models.FloatField()
    retreat_duration = models.IntegerField()
    payment_details = models.TextField()
    booking_date = models.DateTimeField(auto_now_add=True)
