

# file write

# traditional/regular  way to open the file
fw = open("clients.txt","w")

fw.write("python programming\n")
fw.write("bash scripting\n")

fw.close() # closing in required


# context manager
# It is NOT required to close the file.. file will be closed automatically
# In socket programming/network programming/database programming
with open("customers.txt","w") as fw:
    fw.write("scala programming\n")
    fw.write("ansible for automations\n")

'''    
"C:\\Users\\Administrator\\Desktop\\clients.txt"   (or)
"C:/Users/Administrator/Desktop/clients.txt"       (or)
r"C:\Users\Administrator\Desktop\clients.txt"      ( raw string)
'''


