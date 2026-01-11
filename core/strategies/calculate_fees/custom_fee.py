from .hourly_fee import HourlyFeeCalculator
from .penalty_fee import PenaltyCalculator
from .surcharge_fee import SurchargeCalculator


class CustomFeeCalculator:

    def __init__(self):
        self.hourly = HourlyFeeCalculator()
        self.penalty = PenaltyCalculator()
        self.surcharge = SurchargeCalculator()

    def calculate(self, ticket):
        base_amount = self.hourly.calculate(ticket)

        if ticket.exit_time is None:
            base_amount += self.penalty.calculate(ticket)

        return self.surcharge.calculate(base_amount)
