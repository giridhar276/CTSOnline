alist =[10,20,30]
#output : [15,25,35]
#write a python function to increment each element of the list with 5
#output : [15,25,35]

def increment(x):
    return x + 5
alist = [10,20,30]
blist = []
for val in alist:
    blist.append(increment(val))
print(blist)
##############################
#2nd method    map + lambda
alist = [10,20,30]
#          map( function , list )
print(list(map(lambda x : x + 5 ,alist)))
#################################
# 3rd method
#2nd method    map + lambda
alist = [10,20,30]
def increment(x):
    return x + 5
print(list(map(increment ,alist)))
########################################
#4th method  - list comprehension
alist =[10,20,30]
blist = [ val + 5  for val in alist]
