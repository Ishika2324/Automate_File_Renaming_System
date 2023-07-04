import os
from time import sleep


def process_output():
    """
    Function that prints a simple progress bar to make output more attractive
    """
    print("Processing......", end="")
    for i in range(10):  
        sleep(0.2)
        print("." * i, end="")

    print("\nDone processing :)\n")


def arrange(folder, file, ext):
    
    try:
        if os.path.exists(folder):  
            os.chdir(folder)  
            extension = "." + ext  
            j = 0 
            names_of_files = os.listdir()  
            print("This folder contains", len(names_of_files), "files")  

            for i in range(len(names_of_files)):  
                f = open(file)  

                if names_of_files[i].lower() not in f.read().lower() and names_of_files[i] != file:
                    
                    split = os.path.splitext(names_of_files[i])

                    if extension == split[1]:  
                        os.rename(names_of_files[i], str(j) + extension)  
                        j += 1  

                    if extension != split[1]:
                        os.rename(names_of_files[i], names_of_files[i].capitalize())  
                       

                f.close()  

        else:  
            print("The Path you have provided does not exists :(")
            exit()  

    except Exception as e:
        print(e)  

    else:
        print("Task Completed Successfully... :)")  


if __name__ == '__main__':
    directory = input("Enter the Path of the Folder in which you want to Organize files\n")
    
    exception_file = input("Enter the name of the file with extension in which the names of the "
                           "files are written whose name should not be changed\n")
    

    file_extension = input("Enter the extension of the files whose names you want to change\n")
    

    process_output() 

    arrange(directory, exception_file, file_extension)