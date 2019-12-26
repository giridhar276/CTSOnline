# inline function in python is called as lambda
# Instead of calling the function body ..
# function body will be replaced in the function call itself
# ***** lambda is not REPLACMENT of the complete function
#  it is just the replacement of single liner functions


#syntax:
#functioname = lambda variables: expression
getsum = lambda x : x + 10
total = getsum(10)
print(total)



gettotal = lambda x,y : x + y
total = gettotal(10,20)
print(total)


getupper = lambda name : name.upper()
output= getupper("python")
print(output)
