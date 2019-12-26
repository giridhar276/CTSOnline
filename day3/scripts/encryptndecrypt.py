from cryptography.fernet import Fernet

# creating key
key = Fernet.generate_key()
print("Key :",key)
print()



password = "welcome@123"
# converting to byte string
message = password.encode()

f = Fernet(key)
encrypted = f.encrypt(message)
# encrypted password
print(encrypted)
print()

# decrypting from encrypted password
decrypted = f.decrypt(encrypted)
print(decrypted.decode('utf-8'))
