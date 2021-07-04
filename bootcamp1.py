import hashlib

def md5_func(name):
    y=hashlib.md5(name.encode('UTF-8')).hexdigest()
    return y

inputName = input("enter the string")
print(md5_func(inputName))
