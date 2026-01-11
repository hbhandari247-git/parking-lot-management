class TicketMapper:

    @staticmethod
    def to_ticket_response(ticket):
        return {
            "ticket_id": ticket.id,
            "slot_number": ticket.parking_slot.slot_number,
            "floor_number": ticket.parking_slot.floor.floor_number,
            "entry_time": ticket.entry_time,
        }

    @staticmethod
    def to_payment_response(ticket):
        return {
            "amount": ticket.amount,
            "payment_status": ticket.payment_status,
            "exit_time": ticket.exit_time,
        }
