
# HIDING THE PASSWORD
import getpass    #builtin library
password = getpass.getpass("Enter your password :")
print("You entered :", password)


import stdiomask  # third party library
password = stdiomask.getpass("Enter your password :",mask="-")
print("You entered :", password)