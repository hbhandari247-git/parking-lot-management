from django.db import models
from core.enums import SlotType
from .parking_floor import ParkingFloor


class ParkingSlot(models.Model):
    slot_number = models.IntegerField()
    slot_type = models.CharField(
        max_length=20,
        choices=SlotType.choices
    )
    is_available = models.BooleanField(default=True)
    floor = models.ForeignKey(
        ParkingFloor,
        on_delete=models.CASCADE,
        related_name="slots"
    )

    class Meta:
        unique_together = ("slot_number", "floor")

    def __str__(self):
        return f"Slot {self.slot_number} ({self.slot_type}) - Floor {self.floor.floor_number}"
