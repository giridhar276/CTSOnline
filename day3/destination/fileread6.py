
try:
    filename = input("Enter any file name :")
    with open(filename,"r") as fr:
        for line in fr:
            line = line.strip()
            print(line)

    output  = 1 + "hello"            
except FileNotFoundError as error:
    print("File not found")            
    print("System error :", error)
except TypeError as error:
    print("Invalid operations")            
    print("System error :", error)
except Exception as error:
    print("Unknown exception")    
    print("System error :", error)