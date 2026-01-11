from core.enums import PaymentStatus
from core.strategies.calculate_fees.custom_fee import CustomFeeCalculator


class PaymentService:

    def __init__(self):
        self.fee_calculator = CustomFeeCalculator()

    def process_payment(self, ticket):
        amount = self.fee_calculator.calculate(ticket)

        return {
            "amount": amount,
            "status": PaymentStatus.SUCCESS
        }
