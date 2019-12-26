import pymysql
from configparser import ConfigParser
import time
import os
try:
    from openpyxl import Workbook
    wb = Workbook()
    # grab the active worksheet
    ws = wb.active
    parser = ConfigParser()
    parser.read('properties.conf')    
    hostname = parser.get('database_config', 'hostname')
    portno = parser.get('database_config', 'port')
    username = parser.get('database_config', 'username')
    password = parser.get('database_config', 'password')
    database = parser.get('database_config','database')
    filename = parser.get('file_config','filename')
    excelfile = time.strftime("%d_%b_%Y.xlsx")
     
    with pymysql.connect(host=hostname,port =int(portno),user=username,password=password ,database=database ) as db:
        if os.path.exists(excelfile):
            os.unlink(excelfile)
        else:
            query = "select * from realestate1"
            db.execute(query)
            for record in db.fetchall():
                ws.append(record)
            wb.save(excelfile)
            
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
    
            