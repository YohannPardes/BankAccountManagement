from datetime import datetime


class Transaction:

    def __init__(self, business_name, date: datetime, amount: int):
        self.date = datetime.strptime(date, "%d/%m/%Y")
        self.amount = amount
        self.business = business_name

    def __eq__(self, other):
        if self.date == other.date and self.amount == other.amount and self.business == other.business:
            return True
        return False

    def __hash__(self):
        return hash((self.date, self.business, self.amount))
