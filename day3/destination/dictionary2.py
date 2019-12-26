'''
define some dictionary as below

adict = {"emp1":["raj",28] ,"emp2":["ram",34] ,"emp3":["rita",24]}

write a program to check whether the key "emp2" is existing in the list or not
'''


adict = {"emp1":["raj",28] ,"emp2":["ram",34] ,"emp3":["rita",24]}

if "emp20" in adict:
    print("Employee is working")
else:
    print("employee is not working")
    
    
'''
define some list as below

data = ["perl","unix","perl","scala","perl"]

write a program to count the no. of occurences of each item

perl 3
unix 1
scala 1
'''    
data = ["perl","unix","perl","scala","perl"]
for item in set(data):
    print(item.ljust(6) , data.count(item))