from core.services.ticket_service import TicketService
from core.services.payment_service import PaymentService


from django.utils import timezone

class ExitGateService:
    def __init__(self):
        self.ticket_service = TicketService()
        self.payment_service = PaymentService()

    def process_exit(self, ticket_id):
        ticket = self.ticket_service.get_active_ticket(ticket_id)

        # ✅ SET EXIT TIME FIRST
        ticket.exit_time = timezone.now()
        ticket.save()

        # ✅ NOW calculate payment
        payment = self.payment_service.process_payment(ticket)

        # ✅ Free slot
        slot = ticket.parking_slot
        slot.is_available = True
        slot.save()

        # ✅ Close ticket
        return self.ticket_service.close_ticket(ticket, payment)

