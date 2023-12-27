import os
from time import sleep
import maskpass
password_check = False
re_enter_pass = True
while password_check == False:
    while re_enter_pass == True:
        user_name = str(input("Hello person, what would you like your username to be? \n"))
        password = maskpass.askpass(mask="")
        if len(user_name) and len(password) != 0:
            f = open("User_Data.txt","a") 
        if len(password) < 8:
            print("Please enter a password with 8 minimum letters.\n")
        else:
            f.write(f"{user_name}; {password}\n")
            print("Password stored.")
            sleep(2)
            os.system('cls')
            sleep(2)
            re_enter = input("Would you like to enter a new password? (Y/N)\n")
            if re_enter == "Y":
                re_enter_pass = True
                os.system('cls')
            elif re_enter == "N":
                re_enter_pass = False
                password_check = True
                break


    