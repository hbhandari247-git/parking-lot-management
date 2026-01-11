from django.db import models
from core.enums import VehicleType


class Vehicle(models.Model):
    vehicle_number = models.CharField(
        max_length=20,
        unique=True
    )
    vehicle_type = models.CharField(
        max_length=20,
        choices=VehicleType.choices
    )

    def __str__(self):
        return f"{self.vehicle_number} ({self.vehicle_type})"
