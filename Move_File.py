import os
import shutil

from_dir= "C:/Users/auser/Downloads"
to_dir="C:/Users/auser/OneDrive - Kensington Mortgage Company Limited/Desktop"
to_dir2="C:/Users/auser/OneDrive - Kensington Mortgage Company Limited/Desktop"

list_of_files = os.listdir(from_dir)
#print(list_of_files)

for file_name in list_of_files:

    name, extension = os.path.splitext(file_name)


    if extension == '':
        continue
    if extension in ['.gif','.png','jpg','.jpg','.jfif']:
        path1= from_dir + '/' + file_name
        path2= to_dir + '/' + "Image_File"
        path3= to_dir + '/' + "Image_File"
    
    if extension in [".pdf"]:
        path4= from_dir + '/' + file_name
        path5= to_dir2 + '/'+ "pdf_File"
        path6= to_dir2 + '/'+ "pdf_File"
        



        if os.path.exists(path2):
            print("Moving" + file_name + "......")

            shutil.move(path1,path3)

        else:
            os.makedirs(path2)
            print("Moving" + file_name + "......")

            shutil.move(path1,path3)

        if os.path.exists(path5):

            print("Moving" + file_name + "......")

            shutil.move(path4,path6)

        else: 
            os.makedirs(path5)
            print("Moving" + file_name + "......")

            shutil.move(path4,path6)
        
    
        
        




