#Q) WAP in python to copy the content of "demo.txt" file into "new.txt" file with proper exception 

def copy_file():
    try:
        with open(r"C:\Users\Aryan\OneDrive\Documents\Python pyqs codes\coping_file\demo.txt","r") as src:
            with open(r"C:\Users\Aryan\OneDrive\Documents\Python pyqs codes\coping_file\new.txt","w") as dest :
                for line in src:
                    dest.write(line);
        print("File is Copied Successfully")
    except FileNotFoundError :
        print("Error : 'demo.txt' not found ")
    except PermissionError :
        print("Error : Permission Denied ")
    except Exception as e:
        print(f"Error : {e} ")


copy_file();
