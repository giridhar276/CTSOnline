import pymysql
from configparser import ConfigParser
import csv
import os
try:
    parser = ConfigParser()
    parser.read('properties.conf')    
    hostname = parser.get('database_config', 'hostname')
    portno = parser.get('database_config', 'port')
    username = parser.get('database_config', 'username')
    password = parser.get('database_config', 'password')
    database = parser.get('database_config','database')
    filename = parser.get('file_config','filename')
     
    with pymysql.connect(host=hostname,port =int(portno),user=username,password=password ,database=database ) as db:
        if os.path.isfile(filename) and os.path.getsize(filename) > 0:
            with open(filename,"r") as fr:
                reader = csv.reader(fr)
                for line in reader:
                    print(line)
                    query = "insert into realestate1 values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(*line)
                    #print(query)
                    db.execute(query)
                    #print(db.rowcount , " record inserted")
        else:
            print("file doesn't exist")       
except pymysql.MySQLError as err:
    print(err)            
except pymysql.OperationalError as err:
    print("Please check your credentials")    
    print(err)
except pymysql.IntegrityError as err:
    print("please check with foreign or primay keys")    
    print(err)
except Exception as err:
    print("unknown err")    
    print(err)
    
            