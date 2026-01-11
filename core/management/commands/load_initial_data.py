from django.core.management.base import BaseCommand
from core.models import ParkingFloor, ParkingSlot
from core.enums import SlotType


class Command(BaseCommand):
    help = "Load initial parking floors and slots"

    def handle(self, *args, **kwargs):
        floors = [1, 2]

        for floor_no in floors:
            floor, _ = ParkingFloor.objects.get_or_create(
                floor_number=floor_no
            )

            for slot_no in range(1, 11):
                ParkingSlot.objects.get_or_create(
                    floor=floor,
                    slot_number=slot_no,
                    defaults={
                        "slot_type": SlotType.CAR_SLOT,
                        "is_available": True
                    }
                )

        self.stdout.write(self.style.SUCCESS("Initial parking data loaded"))
