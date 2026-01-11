from django.db import models
from django.utils import timezone
from core.enums import PaymentStatus
from .vehicle import Vehicle
from .parking_slot import ParkingSlot


class Ticket(models.Model):
    vehicle = models.ForeignKey(
        Vehicle,
        on_delete=models.CASCADE
    )
    parking_slot = models.ForeignKey(
        ParkingSlot,
        on_delete=models.PROTECT
    )
    entry_time = models.DateTimeField(default=timezone.now)
    exit_time = models.DateTimeField(null=True, blank=True)
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )
    payment_status = models.CharField(
        max_length=20,
        choices=PaymentStatus.choices,
        default=PaymentStatus.PENDING
    )

    def __str__(self):
        return f"Ticket {self.id} - {self.vehicle.vehicle_number}"
