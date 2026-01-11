class ParkingException(Exception):
    """Base exception for parking lot domain"""
    pass


class NoAvailableSlotException(ParkingException):
    def __init__(self, message="No parking slots available"):
        super().__init__(message)


class InvalidTicketException(ParkingException):
    def __init__(self, message="Invalid or already closed ticket"):
        super().__init__(message)
