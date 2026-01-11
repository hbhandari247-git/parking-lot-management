from django.db import models

class SlotType(models.TextChoices):
    CAR_SLOT = "CAR_SLOT", "car_slot"
    EV_SLOT = "EV_SLOT", "ev_slot"
    TRUCK_SLOT = "TRUCK_SLOT", "truck_slot"
