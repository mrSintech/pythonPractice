import webbrowser

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

        self.cell_height = 40
        self.filename = None

    def set_font(self, font: str = "Times", size: int = 24, style=None):
        pdf = self.pdf_file
        if style:
            pdf.set_font(family=font, size=size, style=f"{style}")
        else:
            pdf.set_font(family=font, size=size)

    @property
    def pdf_file(self):
        if not self._pdf_file:
            self._pdf_file = FPDF(orientation="P", unit='pt', format="A4")
            self.set_font()
        return self._pdf_file

    def build_header(self):
        pdf = self.pdf_file
        self.set_font(style="B")
        pdf.image("static/house.png", w=40, h=40)
        pdf.cell(w=0, h=self.cell_height*2, txt="Flatmates Bill", border=1, align="C", ln=1)

    def build_middle(self):
        pdf = self.pdf_file
        self.set_font(size=15, style="B")
        pdf.cell(w=100, h=40, txt="period: ")
        pdf.cell(w=100, h=40, txt=self.bill.period,)
        pdf.cell(h=self.cell_height, w=0, txt=f"Total : {self.bill.amount}$", ln=1)

    def build_flatmates_pay(self):
        pdf = self.pdf_file
        self.set_font(size=12, style="B")
        for flatmate in self.bill.flatmates:
            pdf.cell(h=self.cell_height, w=100, txt=flatmate.name)
            pdf.cell(h=self.cell_height, ln=1, w=100, txt=str(flatmate.pays(self.bill))+"$")

    def output(self):
        pdf = self.pdf_file
        self.filename = f"{self.bill.period}.pdf"
        pdf.output(self.filename)
        webbrowser.open(self.filename)  # automatically open generated pdf file

    def generate(self):
        pdf = self.pdf_file

        pdf.add_page()
        self.build_header()
        self.build_middle()
        self.build_flatmates_pay()
        self.output()


if __name__ == "__main__":
    the_bill = Bill(amount=120, period="March 2020")
    john = Flatmate(name="John", days_in_house=11)
    marry = Flatmate(name="Marry", days_in_house=25)
    linda = Flatmate(name="Linda", days_in_house=19)
    the_bill.add_flatmate(john, marry, linda)

    PdfReport(the_bill).generate()

