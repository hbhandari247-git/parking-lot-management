from django.utils import timezone
from core.models import Ticket
from core.exceptions import InvalidTicketException


class TicketService:

    def create_ticket(self, vehicle, slot):
        return Ticket.objects.create(
            vehicle=vehicle,
            parking_slot=slot
        )

    def get_active_ticket(self, ticket_id):
        try:
            ticket = Ticket.objects.get(id=ticket_id)
        except Ticket.DoesNotExist:
            raise InvalidTicketException("Ticket not found")

        if ticket.exit_time is not None:
            raise InvalidTicketException("Ticket already closed")

        return ticket

    def close_ticket(self, ticket, amount, status):
        ticket.exit_time = timezone.now()
        ticket.amount = amount
        ticket.payment_status = status
        ticket.save()
        return ticket
