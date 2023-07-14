name=input("Hey, what is your name? ")
age=int(input(f"ok, {name}, how old are you? "))
if age<16:
    print("You can't drive",name)
elif age<18:
    print("You can't vote",name)
elif age<25:
    print("You can't rent a car",name)
elif age>=25:
    print("You can do anything that's legal",name)
else:
    print(0)