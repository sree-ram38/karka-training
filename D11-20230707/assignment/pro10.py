names=input("enter the name : ")
a=int(input("enter the age : "))
print(f"Hey, What's your name? (sorry, I keep forgetting.){names}")
print(f"ok {names} how old are you? {a}")
print("\n")
if a<16:
    print(f"you can't drive{names}")
elif a>=16 and a<=17:
    print(f"You can drive but not vote{ names}")
elif a>=18 and a<=24:
    print(f"You can vote but not rent car a {names}")
elif a>=25:
    print(f"You can do pretty much anything {names}")
else:
    print("error")