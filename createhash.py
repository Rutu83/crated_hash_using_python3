import hashlib
x="lover"
y=hashlib.md5(x.encode('utf-8')).hexdigest()
print("Your output is:"+y)