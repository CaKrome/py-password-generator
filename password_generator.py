import random
import string

print("Info: Enter 1 for digits only, 2 for digits plus lowercase letters and 3 for digits plus uppercase letters, 4 for uppercase letters only, 5 for lowercase letters only, 6 for letters and 7 for letters plus digits.")
cont = "yes"
while cont[0] == "y":
    try:
        selection = int(input("Please choose the password combination: "))
        if selection <= 7 and selection > 0:
            r = int(input("Please input the length of password you want: "))

            def password(cha, r):
                pwdlist = []
                for _ in range(random.randint(r, r)):
                    pwd = random.choice(cha)
                    pwdlist.append(pwd)
                    passwd = "".join(pwdlist)
                return passwd
            if selection == 1:
                cha = string.digits
                print(password(cha, r))
            elif selection == 2:
                cha = string.digits + string.ascii_lowercase
                print(password(cha, r))
            elif selection == 3:
                cha = string.digits + string.ascii_uppercase
                print(password(cha, r))
            elif selection == 4:
                cha = string.ascii_uppercase
                print(password(cha, r))
            elif selection == 5:
                cha = string.ascii_lowercase
                print(password(cha, r))
            elif selection == 6:
                cha = string.ascii_letters
                print(password(cha, r))
            elif selection == 7:
                cha = string.ascii_letters + string.digits
                print(password(cha, r))
        else:
            print("Please enter 1 to 7 only")
        cont = input(
            "Do you want generate another password(yes or y to continue, any other input to quit)? ")
    except:
        print("You entered something wrong.")
