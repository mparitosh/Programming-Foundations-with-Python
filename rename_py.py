import os
import re

def rename_files():
    # (1) get file names from a folder
    file_list = os.listdir(r"C:\Users\Paritosh\Desktop\EmergStorage\Py\prank")

    # print(file_list)
    saved_path = os.getcwd()
    print("Current Working Directory is " + saved_path)
    os.chdir(r"C:\Users\Paritosh\Desktop\EmergStorage\Py\prank")
    
    # (2) for each file, rename file name
    for file_name in file_list:
       new_name = re.sub('[0-9]', '', file_name)
       os.rename(file_name,new_name)
       print (new_name)
rename_files()
