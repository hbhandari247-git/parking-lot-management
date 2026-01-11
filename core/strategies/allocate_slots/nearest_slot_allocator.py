from core.models import ParkingSlot
from .base import SlotAllocator


class NearestSlotAllocator(SlotAllocator):

    def allocate(self, vehicle_type):
        return (
            ParkingSlot.objects
            .filter(is_available=True)
            .select_related("floor")
            .order_by("floor__floor_number", "slot_number")
            .first()
        )
