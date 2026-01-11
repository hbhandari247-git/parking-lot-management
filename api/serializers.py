from rest_framework import serializers
from core.enums import VehicleType
from core.models import Vehicle


class VehicleRequestSerializer(serializers.Serializer):
    vehicle_number = serializers.CharField(max_length=20)
    vehicle_type = serializers.ChoiceField(choices=VehicleType.choices)

    def create(self, validated_data):
        vehicle, _ = Vehicle.objects.get_or_create(
            vehicle_number=validated_data["vehicle_number"],
            defaults={"vehicle_type": validated_data["vehicle_type"]}
        )
        return vehicle

class ExitRequestSerializer(serializers.Serializer):
    ticket_id = serializers.IntegerField()

class TicketResponseSerializer(serializers.Serializer):
    ticket_id = serializers.IntegerField()
    slot_number = serializers.IntegerField()
    floor_number = serializers.IntegerField()
    entry_time = serializers.DateTimeField()

class PaymentResponseSerializer(serializers.Serializer):
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    payment_status = serializers.CharField()
    exit_time = serializers.DateTimeField()
