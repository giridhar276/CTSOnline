import calendar   

print(calendar.month(2019,12))


print(calendar.calendar(2019))


import glob

for file in glob.glob("C:\\Users\\Administrator\\Desktop\\day3\\scripts\\*.py"):
    print(file)
    
    
    
# invoking system commands in python    
import subprocess

output= subprocess.getoutput("python abc.py")    
print(output)