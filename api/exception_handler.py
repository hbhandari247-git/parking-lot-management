from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status

from core.exceptions import (
    NoAvailableSlotException,
    InvalidTicketException
)


def global_exception_handler(exc, context):
    # Let DRF handle standard exceptions first
    response = exception_handler(exc, context)

    if isinstance(exc, NoAvailableSlotException):
        return Response(
            {"error": str(exc)},
            status=status.HTTP_409_CONFLICT
        )

    if isinstance(exc, InvalidTicketException):
        return Response(
            {"error": str(exc)},
            status=status.HTTP_400_BAD_REQUEST
        )

    return response
