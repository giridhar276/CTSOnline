


# import string library function 
import string 
import random

# Storing the value in variable result 

lower = string.ascii_lowercase
lowerlist = list(lower)
upper = string.ascii_uppercase
upperlist = list(upper)


numbers = string.digits
numlist = list(numbers)

symbols = string.punctuation
symlist = list(symbols)

random.shuffle(list(lower))
random.shuffle(list(upper))
random.shuffle(list(numbers))
random.shuffle(symlist)

shuffled = lowerlist + upperlist + numlist + symlist
sampling = random.choices(shuffled, k=8)

password = "".join(sampling)
print(password)