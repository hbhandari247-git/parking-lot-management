from django.db import models

class VehicleType(models.TextChoices):
    BIKE = "BIKE", "Bike"
    CAR = "CAR", "Car"
    TRUCK = "TRUCK", "Truck"
