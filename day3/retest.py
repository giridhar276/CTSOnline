import re
regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
email = "jkumar025@gmail.com"

if re.search(regex,email):
    print("valid email")
else:
    print("Invalid email")
    