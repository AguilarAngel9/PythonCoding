# Flatmates Bill App

import fpdf
import sys

class Bill:
    """ 
    Object thaat contains data about a bill, such as
    total amount, and period of the bill.
    """
    
    def __init__(self, amount, period) -> None:
        self.amount = amount
        self.period = period

class Flatmate:
    """
    Creates a flatname person who live in the flat and pays a share of the bill.
    """

    def __init__(self, name, days_in_house) -> None:
        self.name = name
        self.days_in_house = days_in_house
    
    # Methods
    def pays(self, bill, flatmate2):
        weight = self.days_in_house / (flatmate2.days_in_house + self.days_in_house)
        to_pay = bill.amount * weight
        return to_pay

class PDFReport:
    """
    Creates a PDF file that contain data abour the flatmates such as their names,
    their due amount and the period of the bill.
    """
    
    def __init__(self, filename) -> None:
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
         
        pass
        
bill = Bill(amount = 120, period = 'March 2020')
john = Flatmate(name = 'John', days_in_house = 20)
mary = Flatmate(name = 'Mary', days_in_house = 25)

print(f'Jonh pays: {john.pays(bill=bill, flatmate2=mary)}')
print(f'Mary pays: {mary.pays(bill=bill, flatmate2=john)}')