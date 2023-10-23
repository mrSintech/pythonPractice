class Flatmate:
    """
    Creates a flatmate person who lives in the flat and pays a share of the bill
    """

    def __init__(self, name: str, days_in_house: int):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill):
        weight = self.days_in_house / bill.sum_of_all_flatmates_days()
        flatmate_pay = bill.amount * weight
        return round(flatmate_pay, 2)

    def __repr__(self):
        return f"{self.name} has been in house for {self.days_in_house} days"


class Bill:
    """
    Objects that contains data about a bill, such as total amount and period of the bill.
    """
    def __init__(self, amount: float, period: str):
        self.amount = amount
        self.period = period

        self.flatmates = []

    def __repr__(self):
        return f"the bill of {self.period} is {self.amount}$ and {self.flatmates}"

    def __str__(self):
        flatmates = f"{'name':<9} | {'days':<4} | {'pays':<9} in {self.period}\n"
        for flatmate in self.flatmates:
            flatmates += f"{flatmate.name:<9} | {flatmate.days_in_house:<4} | {flatmate.pays(self):<9}$\n"

        return flatmates

    def add_flatmate(self, *flatmates: Flatmate) -> list:
        for flatmate in flatmates:
            self.flatmates.append(flatmate)

        return self.flatmates

    def sum_of_all_flatmates_days(self) -> int:
        return sum(day.days_in_house for day in self.flatmates)
