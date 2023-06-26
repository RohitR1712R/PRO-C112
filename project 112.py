import os
import shutil

from_dir="C:/Users/Lenovo/Downloads"
to_dir="D:/Document_Files"

list_of_files=os.listdir(from_dir)
#print(list_of_files)

for file_Name in list_of_files:
    path,ext=os.path.splitext(file_Name)
    #print(path)
    if ext == " ":
        continue

    if ext in [".txt", ".doc", ".docx", ".pdf"]:
        path1 = from_dir + "/" + file_Name
        path2 = to_dir
        path3 = path2 + "/" + file_Name

        if os.path.exists(path2):
            print("Folder already exists")
            print("Moving the Files")
            shutil.move(path1, path3)
        
        else:
            print("Creating a new folder")
            os.mkdir(path2)
            print("Moving the Files")
            shutil.move(path1, path3)