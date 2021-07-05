import hashlib

password = input("enter the string")
dk = hashlib.pbkdf2_hmac('md5', password.encode('UTF-8'), b'salt', 100000)
print(dk.hex())
