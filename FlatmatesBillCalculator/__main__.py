class Bill:
    """
    Objects that contains data about a bill, such as total amount and period of the bill.
    """
    def __init__(self, amount: int, period: str):
        self.amount = amount
        self.period = period


class Flatmate:
    """
    Creates a flatmate person who lives in the flat and pays a share of the bill
    """
    
    def __init__(self, name: str, days_in_house: int):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill:  Bill):
        return bill.amount / 2


class PdfReport:
    """
    Creates a PDF file that contains data about flatmates such as
    their name or their due amount and the period of the bill.
    """
    
    def __init__(self, filenames: str, bill: Bill):
        self.filenames = filenames
        self.bill = bill

    def generate(self, flatmates: tuple, bill: Bill):
        ...


the_bill = Bill(amount=120, period="March 2020")
john = Flatmate(name="John", days_in_house=20)
marry = Flatmate(name="Marry", days_in_house=25)

print(john.pays(the_bill))
