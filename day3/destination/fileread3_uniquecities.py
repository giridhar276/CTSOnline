'''
"http://samplecsvs.s3.amazonaws.com/Sacramentorealestatetransactions.csv"
'''
import urllib.request
import csv
url = "http://samplecsvs.s3.amazonaws.com/Sacramentorealestatetransactions.csv"
filename = url.split("/")[-1]
# downloading the file
urllib.request.urlretrieve(url,filename)

# using set
# Uisng csv  it is not required to strip and split ... csv will take care of this
cityset = set()
with open(filename,"r") as fobj:
    # will convert fobj to csv reader object
    reader = csv.reader(fobj)
    for line in reader:
        # Here line is automatically converted to list
        cityset.add(line[1])
    for city in cityset:
        print(city)
        

      