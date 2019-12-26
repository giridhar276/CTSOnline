'''
write a program to display the total count of 

Residential flats
non Residential flats

Output:
Residential flats     : xxx
non Residential flats : xx
'''
import urllib.request
import csv
url = "http://samplecsvs.s3.amazonaws.com/Sacramentorealestatetransactions.csv"
filename = url.split("/")[-1]
# downloading the file
urllib.request.urlretrieve(url,filename)

# using set
# Uisng csv  it is not required to strip and split ... csv will take care of this
rescount = 0
nonrescount = 0
with open(filename,"r") as fobj:
    # will convert fobj to csv reader object
    reader = csv.reader(fobj)
    for line in reader:
        if line[7] == "Residential":
            rescount =rescount + 1
        else:
            nonrescount = nonrescount + 1

print("Residential count     :", rescount)   
print("Non residential count :", nonrescount)         
            

