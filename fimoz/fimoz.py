import random
import time

logins = []
passwords = []


#colors

def out_red(text):
    print("\033[31m {}" .format(text))

def out_yellow(text):
    print("\033[33m {}" .format(text))

def out_blue(text):
    print("\033[34m {}" .format(text))

def out_green(text):
    print("\033[32m {}" .format(text))

#func

def registration_or_login():
    while True:
        loginorregister = int(input(out_blue("Choose login or register\n1 - Register\n2 - Login\n")))
        if loginorregister == 1:
            login = input(out_blue("Type your name\n"))
            password = input(out_blue("Type your password\n"))
            if logins.count(login) == 0 and passwords.count(password) == 0:
                logins.append(login)
                passwords.append(password)
            else:
                out_blue("error, login or password is repeats\n")

        if loginorregister == 2:
            login = input(out_blue("Type your name\n"))
            password = input(out_blue("Type your password\n"))
            if logins.index(login) == passwords.index(password):
                print("Login Successful")
                break
            else:
                print("Login Failed")

def loading():
    out_red(
        "░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█\n█░██░██░██░██░██░██░██░██░██░░░░░░░░░░█\n█░██░██░██░██░██░██░██░██░██░░░░░░░░░░█\n█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n░░█░░░░█▀▀▀█░█▀▀█░█▀▀▄░▀█▀░█▄░░█░█▀▀█░░\n░░█░░░░█░░░█░█▄▄█░█░░█░░█░░█░█░█░█░▄▄░░\n░░█▄▄█░█▄▄▄█░█░░█░█▄▄▀░▄█▄░█░░▀█░█▄▄█░░\n░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n")

    time.sleep(2)





#code



loading()

registration_or_login()

loading()

out_yellow("░░░░░░▄▄▄▄███▄▄▄▄░░░░░░░░░░░░░\n░░░▄▄█▀░░░░░░░░░▀▀▄▄░░░░░░░░░░\n░░█▀░░░░░░░░░░░░░░░▀█▄░░░░░░░░\n░█▀░░░░░░░░░░░░░░░░░░█▄░░░░░░░\n██░░░░░░░░░░░░░░░░░░░░█▄░░░░░░\n█░░░░░░░░░░░░░░░░░░░░░░█▄░░░░░\n██░░░░░░░░░░░░▄▄▄▄▄█▀▀▀██▄░░░░\n▀█░░░░░░░░░▄█▀▀░░▀▀█▄░░░░█▄░░░\n░█▄░▄░░░░░▄█░░░░░░░░█▄░█░░█░░░\n░▄█▄██▄░░░█▄░░██░░░░██▄▄▄██░░░\n░████░▀▀░░░█▄░░░░░░▄█░░░░░██░░\n░█░░██▄▄░░░░▀██▄▄██▀▄▄▄▄▄▄█░░░\n░░▄█▀░░░░░░░░░▄▄██▀▀▀▀▀▀▀░▀█▄░\n░░▀█░░░░░░░▄█▀▀░░░░░░░░░░░░░█▄\n░░░▀█▄▄█▀░█▀░░░░░░░░░░░░░░░▄█▀\n░░░░░░██░▄█░░░█▀██▀▀█▀██▀▀▀▀░░\n░░░░░▄█░░▀█░░▀█░█░░██░██░░░░░░\n░░░░██▀█▄░▀█▄░▀▀████▀▀██░░░░░░\n░░░░█░░░▀▀█▄▀█▄▄▄▄▄▄▄▄██▄░░░░░\n")

out_yellow("Hello I am Homer Simpson.\n")





