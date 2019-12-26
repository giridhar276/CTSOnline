'''
write a program to replace all the lines containing 

SACRAMENTO  with CHENNAI
RIO LINDA   with HYDERABAD

and write the output to backup.csv
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
    with open("backup.csv","w") as fw:
        for line in fobj:
            line = line.strip()
            line = line.replace("SACRAMENTO","CHENNAI")
            line = line.replace("RIO LINDA","HYDERABAD")
            fw.write(line + "\n")
