'''
write a progra to read the realestate.csv and display the file content line by line
'''
# download the file
import urllib.request
url = "http://samplecsvs.s3.amazonaws.com/Sacramentorealestatetransactions.csv"
filename = url.split("/")[-1]
# downloading the file
urllib.request.urlretrieve(url,filename)


with open(filename,"r") as fobj:
    for line in fobj:
        #remove white spaces if you have any
        line = line.strip()
        print(line)
        
 

#method2
import csv
with open(filename,"r") as fobj:
    #converting file object to csv object
    reader = csv.reader(fobj)        
    for line in reader:
        print(line)
        

import pandas
df = pandas.read_csv("http://samplecsvs.s3.amazonaws.com/Sacramentorealestatetransactions.csv")
print(df)

        