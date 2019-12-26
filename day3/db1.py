import pymysql

hostname = 'localhost'
portno = 3306
username = 'root'
password = 'india@123'

with pymysql.connect(host=hostname,port =portno,user=username,password=password) as db:
    print(db)
