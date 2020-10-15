 import hashlib

x=input("Enter your string:")
y=hashlib.md5(x.encode('utf-8')).hexdigest()
print("Your output is:"+y)
