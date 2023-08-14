import os
import pandas as pd


def from_excel(path_to_excel):
    """
    get the data from the Excel spreadsheet to a csv file
    """
    data = pd.read_excel(path_to_excel)
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


def get_from_file(path_file):
    """
    process all the Excel files in a folder
    """
    for path in get_excel_from_folder(path_file):
        print(path)
        from_excel("lol")


def get_data_from_row(row, row_names):
    pass


if __name__ == "__main__":
    # name : (how much, categories)
    example_dict = {
        """מש - קר בע"מ""": 9.2,
        """קמפוס מרקט""": 35.36,
    }

    from_excel(r"כרטיסי אשראי_08082023_1034.xlsx")
