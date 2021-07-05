import hashlib

inData = input("Enter the string")
print("MD5 hash =",hashlib.md5(inData.encode('UTF-8')).hexdigest())
print("SHA1 hash =",hashlib.sha1(inData.encode('UTF-8')).hexdigest())
print("SHA256 hash =",hashlib.sha256(inData.encode('UTF-8')).hexdigest())

