from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from api.serializers import VehicleRequestSerializer, TicketResponseSerializer
from core.services.entry_gate_service import EntryGateService
from core.mappers.ticket_mapper import TicketMapper


class EntryAPIView(APIView):

    def post(self, request):
        serializer = VehicleRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        vehicle = serializer.save()

        ticket = EntryGateService().process_entry(vehicle)

        response_data = TicketMapper.to_ticket_response(ticket)
        return Response(response_data, status=status.HTTP_201_CREATED)
