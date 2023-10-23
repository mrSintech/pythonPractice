from FlatmatesBillCalculator.core import Flatmate, Bill
from FlatmatesBillCalculator.pdf_generator import PdfReport

if __name__ == "__main__":
    # CLI
    bill_amount = input("Hey user, enter the house bill amount: ")
    bill_period = input("what month is this bill for? (e.g April 2023): ")
    house_bill = Bill(amount=float(bill_amount), period=bill_period)

    population = input("how many people are living in that house: ")

    for i in range(1, int(population)+1):
        name = input(f"Enter person #{i} name: ")
        days = input(f"in that period How many days person #{i} was in the house: ")
        flatmt = Flatmate(name=name, days_in_house=int(days))
        house_bill.add_flatmate(flatmt)

    print(house_bill)
    pdf_url = PdfReport(house_bill).generate()
    print(f"Download Pdf: {pdf_url}")
