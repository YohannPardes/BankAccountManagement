from datetime import datetime


class Transaction:

    def __init__(self, business_name, date: datetime, amount: int):
        self.date = datetime.strptime(date, "%d/%m/%Y")
        self.amount = amount
        self.business = business_name
