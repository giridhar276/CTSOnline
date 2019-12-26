

with open("numbers.txt","w") as fw :
    for line in range(50,0,-1) :
        fw.write(str(line) + "\n")