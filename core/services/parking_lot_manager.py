from core.services.entry_gate_service import EntryGateService
from core.services.exit_gate_service import ExitGateService


class ParkingLotManager:

    def __init__(self):
        self.entry_service = EntryGateService()
        self.exit_service = ExitGateService()

    def vehicle_entry(self, vehicle):
        return self.entry_service.process_entry(vehicle)

    def vehicle_exit(self, ticket_id):
        return self.exit_service.process_exit(ticket_id)
