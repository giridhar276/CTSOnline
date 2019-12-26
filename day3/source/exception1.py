try:
    filename = input("Enter any file name :")
    with open(filename,"r") as fr:
        for line in fr:
            line = line.strip()
            print(line)

    output  = 1 + "hello"            
except (FileNotFoundError,TypeError,ValueError) as error:    
    print("System error :", error)
except Exception as error:
    print("Unknown exception")    
    print("System error :", error)
