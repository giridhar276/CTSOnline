import re

line  = "The rain in Spain"
x = re.findall("ai", line)
print(x)


line = "The rain in Spain"
x = re.findall("Portugal", line)
print(x)


line = "The rain in Spain"
x = re.search("\s", line)
print("The first white-space character is located in position:", x.start())


line = "The rain in Spain"
x = re.search("Portugal", line)
print(x)



line = "The rain in Spain"
x = re.sub("\s", "9", line)
print(x)


import re
string = 'hello 12 hi 89. Howdy 34'
pattern = '\d+'
result = re.findall(pattern, string)
print(result)


import re
string = 'Twelve:12 Eighty nine:89.'
pattern = '\d+'
result = re.split(pattern, string)
print(result)





import re
# multiline string
string = 'abc    12de 23 \n f45 6'
# matches all whitespace characters
pattern = '\s+'
# empty string
replace = ' '
new_string = re.sub(pattern, replace, string)
print(new_string)



import re
string = '39801 356, 2102 1111'
# Three digit number followed by space followed by two digit number
pattern = '(\d{3}) (\d{2})'
# match variable contains a Match object.
match = re.search(pattern, string)
if match:
  print(match.group())
else:
  print("pattern not found")





import re

regex = '^[\w]+@[\w]+'

email = "giridhar276@gmail.c33om"

if re.search(regex,email):
    print("valid email")
else:
    print("Invalid email")


# giridhar.s@gmail.com
# giridhar_s@gmail.com
# giri@gmail.com
# 123@gmail.com
  giri.s@cts.in
            .us
            .com
            cts-us.com
            cts-inc.com
            cts.ltd.com
                cts.info     X



import re
regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
email = "jkumar025@gmail.com"

if re.search(regex,email):
    print("valid email")
else:
    print("Invalid email")
    
    
    
    
    
