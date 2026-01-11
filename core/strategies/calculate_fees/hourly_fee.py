from django.utils import timezone


class HourlyFeeCalculator:

    RATE_PER_HOUR = 20

    def calculate(self, ticket):
        duration = ticket.exit_time - ticket.entry_time
        hours = max(1, int(duration.total_seconds() // 3600))
        return hours * self.RATE_PER_HOUR
