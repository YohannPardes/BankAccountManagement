from modules.Utils import get_from_folder
from modules.Business import Business
from modules.Categories import *
import os.path

# initiate the category manager
category_manager = CategoryManager(os.getcwd()+"/Data/Categories.txt")

#extracting all the data
get_from_folder(os.getcwd()+"/Data")

#trier chaque Business dans une categorie
