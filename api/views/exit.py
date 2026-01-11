from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from api.serializers import ExitRequestSerializer
from core.services.exit_gate_service import ExitGateService
from core.mappers.ticket_mapper import TicketMapper


class ExitAPIView(APIView):

    def post(self, request):
        serializer = ExitRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        ticket_id = serializer.validated_data["ticket_id"]

        ticket = ExitGateService().process_exit(ticket_id)

        response_data = TicketMapper.to_payment_response(ticket)
        return Response(response_data, status=status.HTTP_200_OK)
