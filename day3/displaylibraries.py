import time

print(time.time())  # epoch time

print(time.strftime("%d-%b-%Y"))

logfile = time.strftime("%d_%b_%Y.csv")


with open(logfile,"w") as fw:
    fw.write("python\n")