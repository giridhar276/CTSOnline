# reading line by line
with open("numbers.txt","r") as fr :
    for line in fr:
        #remove white spaces at the end of string
        line = line.strip()
        print(line)

# complete file in list format
with open("numbers.txt","r") as fr :
    print(fr.readlines())    
    
#reading the complete file into string    
with open("numbers.txt","r") as fr :
    print(fr.read())
    
# with csv library
import csv
with open("numbers.txt","r") as fr :
    # converting to csv object
    reader = csv.reader(fr)   
    for line in reader:
        print(line)
        
# using pandas
import pandas
df = pandas.read_csv("numbers.txt")
print(df)

        