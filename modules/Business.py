class Business:
    business_list = {}

    def __init__(self, name):
        self.name = name
        self.transaction = set()
        if name not in Business.business_list.keys():
            Business.business_list[name] = self

    def add_transaction(self, transaction):
        self.transaction.add(transaction)

    def __str__(self):
        transaction_string = ""
        total = 0
        for trans in self.transaction:
            transaction_string += str(trans.date) + str(trans.amount) + "\n"
            total += trans.amount

        string = f"""
name :{self.name}

transactions:
{transaction_string}

total: {total}
        """

        return string
