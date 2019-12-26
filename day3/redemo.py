import re

with open("languages.txt") as fr:
    for line in fr:
        line = line.strip()
        if re.search("pyt*hon",line):
            print(line)