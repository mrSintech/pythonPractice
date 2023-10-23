import os
import webbrowser
from fpdf import FPDF
from FlatmatesBillCalculator.core import Bill
from filestack import Client


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

    def build_flatmates_table_header(self):
        pdf = self.pdf_file
        self.set_font(size=12, style="B")
        pdf.cell(h=self.cell_height, w=100, txt="name")
        pdf.cell(h=self.cell_height, w=100, txt="days in house")
        pdf.cell(h=self.cell_height, ln=1, w=100, txt="Pay")

    def build_flatmate_row(self, flatmate):
        pdf = self.pdf_file
        pdf.cell(h=self.cell_height, w=100, txt=flatmate.name)
        pdf.cell(h=self.cell_height, w=100, txt=str(flatmate.days_in_house))
        pdf.cell(h=self.cell_height, ln=1, w=100, txt=str(flatmate.pays(self.bill)) + "$")

    def build_flatmates_table(self):
        self.set_font(size=14)
        self.build_flatmates_table_header()
        for flatmate in self.bill.flatmates:
            self.build_flatmate_row(flatmate)

    def upload_output(self, file):
        client = Client('filestack_apikey')
        new_filelink = client.upload(filepath=file)
        return new_filelink.url

    def output(self):
        pdf = self.pdf_file
        self.filename = f"{self.bill.period}.pdf"
        pdf.output(f"{self.filename}")
        webbrowser.open(self.filename)  # automatically open generated pdf file

    def generate(self):
        self.pdf_file.add_page()
        self.build_header()
        self.build_middle()
        self.build_flatmates_table()
        # self.build_footer()

        # generate output
        org_path = os.getcwd()
        os.chdir("reports")
        self.output()
        pdf_url = self.upload_output(self.filename)
        os.chdir(org_path)
        return pdf_url

