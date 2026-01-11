from core.exceptions import NoAvailableSlotException
from core.services.ticket_service import TicketService
from core.strategies.allocate_slots.nearest_slot_allocator import NearestSlotAllocator


class EntryGateService:

    def __init__(self):
        self.slot_allocator = NearestSlotAllocator()
        self.ticket_service = TicketService()

    def process_entry(self, vehicle):
        slot = self.slot_allocator.allocate(vehicle.vehicle_type)

        if not slot:
            raise NoAvailableSlotException()

        slot.is_available = False
        slot.save()

        return self.ticket_service.create_ticket(vehicle, slot)
