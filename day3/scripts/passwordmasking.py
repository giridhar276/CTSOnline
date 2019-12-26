import getpass

password = getpass.getpass("Enter your password:")
print("password :", password)



import stdiomask

password = stdiomask.getpass("Enter any password :", mask= "*")
print("Password :", password)
