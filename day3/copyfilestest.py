import shutil
import os
source = "C:\\Users\\Administrator\\Desktop\\day3\\source\\"
destination =  "C:\\Users\\Administrator\\Desktop\\day3\\destination\\"
os.chdir(source)
for file in os.listdir(source):
    if os.path.isfile(source + file):
        shutil.copy( file ,destination)