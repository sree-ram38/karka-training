# password=input("Enter the password : ")
# while True:
#     if password>6:
#         print("password is weak")
#     elif password>6 and password<10:
#         print("You need to moderate")
#     elif password>11 and password<15:
#         print("The password is strong")
#     elif password>15:
#         print("The password is very strong")

# import re
# p= input("Input your password : ")

# while True:  
#     if (len(p)<6 or len(p)>12):
#         break
#     elif not re.search("[a-z]",p):
#         break
#     elif not re.search("[0-9]",p):
#         break
#     elif not re.search("[A-Z]",p):
#         break
#     elif not re.search("[$#@]",p):
#         break
#     elif re.search("\s",p):
#         break
# if len(p)>6:
#     print("weak")
# elif len(p)>6 and len(p)<10:
#     print("moderate")
# elif len(p)>11 and len(p)<15:
#     print("strong")
# elif len(p)>15:
#     print("very strong")

password=input("Enter the password: ")

def pwd(password):
    if len(password) < 6:
        return "Weak password, Try another password"
    
    has_uppercase = False
    has_lowercase = False
    has_digit = False

    for i in password:
        if i.isupper():
            has_uppercase=True
        if i.islower():
            has_lowercase=True
        if i.isdigit():
            has_digit=True
    if not (has_uppercase and has_lowercase and has_digit):
        return "Password must contain atleast one upper case letter, one lower case letter and one digit"
    if len(password) >=6 and len(password) <=10:
        return "Moderate password"
    elif len(password) >=11 and len(password) <15:
        return "Strong password"
    elif len(password) >=15:
        return "Very strong password"
    else:
        return "Very strong password"
    
print(pwd(password))