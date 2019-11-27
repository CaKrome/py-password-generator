import string
from random import *
print("Info: Enter 1 for digits only, 2 for digits plus lowercase letters and 3 for digits plus uppercase letters, 4 for uppercase letters only, 5 for lowercase letters only, 6 for letters and 7 for letters plus digits.")
cont = "yes"
while cont[0] == "y":
        try:
                sel = int(input("Please choose the password combination: "))
                if sel <= 7 and sel > 0:
                        r = int(input("Please input the length of password you want: "))
                        def password(cha,r):
                                pwdlist = []
                                for i in range(randint(r,r)):
                                        pwd = choice(cha)
                                        pwdlist.append(pwd)
                                        passwd = "".join(pwdlist)
                                return passwd
                        if sel == 1:
                                cha = string.digits
                                print(password(cha,r))
                        elif sel == 2:
                                cha = string.digits + string.ascii_lowercase
                                print(password(cha,r))
                        elif sel == 3:
                                cha = string.digits + string.ascii_uppercase
                                print(password(cha,r))
                        elif sel == 4:
                                cha = string.ascii_uppercase
                                print(password(cha,r))
                        elif sel == 5:
                                cha = string.ascii_lowercase
                                print(password(cha,r))
                        elif sel == 6:
                                cha = string.ascii_letters
                                print(password(cha,r))
                        elif sel == 7:
                                cha = string.ascii_letters + string.digits
                                print(password(cha,r))
                else:
                        print("Please enter 1 to 7 only")
                cont = input("Do you want generate another password(yes or y to continue, any other input to quit)? ")
        except:
                print("You entered something wrong.")

