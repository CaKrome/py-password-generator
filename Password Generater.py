import string
from random import *
cha = string.ascii_letters + string.digits
try:
	r = int(input("Please input the length of password you want: "))
	pwdlist = []
	for i in range(randint(r,r)):
	    pwd = choice(cha)
	    pwdlist.append(pwd)
	    password = "".join(pwdlist)
	print (password)
except:
	print("Please enter integer only.")
