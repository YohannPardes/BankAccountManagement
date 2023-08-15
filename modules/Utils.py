import os
import pandas as pd
from modules.Business import Business
from modules.Transaction import Transaction


def from_excel(path_to_excel):
    """
    get the data from the Excel spreadsheet to a csv file
    """
    data = pd.read_excel(os.path.abspath("Data/"+path_to_excel))
    data.columns = data.iloc[7]
    data = data.filter(range(8, len(data) - 1), axis=0)
    data = data.reset_index(drop=True)
    data = data[[
        'כרטיס'
        , 'בית עסק'
        , 'תאריך עסקה'
        , 'סכום העסקה']]

    return data


def get_excel_from_folder(path_file):
    """
    filter in all the Excel files from a folder
    """
    return [path for path in os.listdir(path_file) if path.split(".")[-1] == "xlsx"]


def get_from_folder(path_file):
    """
    process all the Excel files in a folder
    """
    for path in get_excel_from_folder(path_file):
        data = from_excel(path)

        columns = list(data.columns)
        for i in range(len(data)):
            name = data[columns[1]][i]
            date = data[columns[2]][i]
            amount = data[columns[3]][i]

            Business(name)
            Business.business_list[name].add_transaction(Transaction(name, date, amount))




if __name__ == "__main__":
    # name : (how much, categories)
    example_dict = {
        """מש - קר בע"מ""": 9.2,
        """קמפוס מרקט""": 35.36,
    }

    # from_excel(r"כרטיסי אשראי_08082023_1034.xlsx")
