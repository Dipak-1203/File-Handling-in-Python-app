import os

def createfile(filename):
    try :     #  exception handling
        with open(filename, 'x') as f:
            print(f"{filename} created successfully.")
            
    except FileExistsError: # exception handling ( popup message if file already exists)
        print("File already exists.")
    except Exception as e: # generic exception handling if any other error occurs
        print(f"An error occurred: {e}")
        
def view_all_file():
    files = os.listdir()  # list all files in current directory
    if not files:
        print("No files found in the current directory.")
    else:
        print("Files found in the current directory:")
        for file in files: # find each file in the directory
            print(file) # print each file name
            
def deletefile(filename):
    try:
        os.remove(filename) # remove the file
        print(f"{filename} deleted successfully.")
        
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
        
        
def readfile(filename):
    try:
        with open (filename , 'r') as f:
            content = f.read() # read the file content
            print(f"content in  file  {content}") # print the file content
            
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")       
        
        
def editfile(filename):
    try:
        with open(filename ,'a') as f: # 'a' mode to append/add/edit content to the file    
           content = input("Enter new content: ") # write new content to the file
           f.write(content + "\n") # add a new line after the content
           print(f"Content added to {filename} successfully.")
           
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
        
def main():
    while True:
        print("FILE HANDLING PROGRAM MENU")
        print("1 : CREATE NEW FILE ")
        print("2 : VIEW  FILE ")
        print("3 : EDIT FILE " )
        print("4 : READ  FILE ")
        print("5 : DELETE  FILE ")
        print("6 : EXIT ")
        choice = input("Enter your choice (1-6): ")
        
        if choice == "1":
            filename = input("Enter a new file name :")
            createfile(filename)
            
        elif choice == "2":
            view_all_file()
            
        elif choice == "5":
            deletefile(filename)
            
        elif choice == "4":
            filename = input("Enter a file do you want to read :")
            readfile(filename)
            
        elif choice == "3":
            filename = input("Enter a file do you want to edit :")
            #new_content = input("Enter new content to add to the file :")
            editfile(filename)
            
        elif choice == "6":
            print("Exiting the program.")
            break    
main()