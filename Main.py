from modules.Utils import from_excel
from modules.Business import Business
from modules.Transaction import Transaction

data = from_excel("modules/כרטיסי אשראי_08082023_1034.xlsx")

columns = list(data.columns)
print(columns)
for i in range(len(data)):
    name = data[columns[1]][i]
    date = data[columns[2]][i]
    amount = data[columns[3]][i]

    B = Business(name)
    Business.business_list[name].add_transaction(Transaction(name, date, amount))

for elem in Business.business_list.values():
    print(elem)
