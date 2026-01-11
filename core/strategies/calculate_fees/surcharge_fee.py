class SurchargeCalculator:

    SURCHARGE_PERCENT = 0.10

    def calculate(self, amount):
        return amount + (amount * self.SURCHARGE_PERCENT)
