from fpdf import FPDF
import ast


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
    def __init__(self, amount: int, period: str):
        self.amount = amount
        self.period = period

        self.flatmates = []

    def __repr__(self):
        return f"the bill of {self.period} is {self.amount}$ and {self.flatmates}"

    def add_flatmate(self, *flatmates: Flatmate) -> list:
        for flatmate in flatmates:
            self.flatmates.append(flatmate)

        return self.flatmates

    def sum_of_all_flatmates_days(self) -> int:
        return sum(day.days_in_house for day in self.flatmates)


class PdfReport:
    """
    Creates a PDF file that contains data about flatmates such as
    their name or their due amount and the period of the bill.
    """
    
    def __init__(self, bill: Bill):
        self.bill = bill
        self._pdf_file = None
        self._global_font = None

    def set_font(self, font: str = "Times", size: int = 24, style: str = "B"):
        pdf = self.pdf_file
        pdf.set_font(family=font, size=size, style=ast.literal_eval(style))

    @property
    def pdf_file(self):
        if not self._pdf_file:
            self._pdf_file = FPDF(orientation="P", unit='pt', format="A4")
            self._pdf_file.set_font(family="Times", size=24, style="B")
        return self._pdf_file

    def pdf_header(self):
        pdf = self.pdf_file


    def generate(self, destination: str = None):
        pdf = self.pdf_file

        pdf.add_page()

        # add text
        pdf.cell(w=0, h=80, txt="Flatmates Bill", border=1, align="C", ln=1)
        pdf.cell(w=100, h=40, txt="period: ", border=1)
        pdf.cell(w=0, h=40, txt="March 2022", border=1, ln=1)
        pdf.cell(w=100, h=40, txt="period: ", border=1)

        pdf.output("bill.pdf")


if __name__ == "__main__":
    the_bill = Bill(amount=120, period="March 2020")
    john = Flatmate(name="John", days_in_house=11)
    marry = Flatmate(name="Marry", days_in_house=25)
    the_bill.add_flatmate(john, marry)

    PdfReport(the_bill).generate()

