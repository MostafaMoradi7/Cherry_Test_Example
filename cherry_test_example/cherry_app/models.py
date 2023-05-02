from django.db import models


# Create your models here.
class Car:
    def __init__(self, car, location, date):
        self.car = car
        self.location = location
        self.date = date