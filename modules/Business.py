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
        for trans in sorted(list(self.transaction), key=lambda x: x.date, reverse=True):
            transaction_string += str(trans.date)[:11] + str(trans.amount) + "₪" + "\n"
            total += trans.amount

        string = f"""
name :{self.name}
transactions:
{transaction_string}
total: {total}
        """

        return string

    @classmethod
    def print_recap(cls):
        for elem in cls.business_list.values():
            print(elem)
