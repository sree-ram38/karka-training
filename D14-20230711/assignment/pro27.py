def addkeychains():
    add=int(input(f"You have {n} keychain. How many to add? "))
    add1=n+add
    print(f"You now have {add1} keychain")
    return add1
def removekeychain():
        rem=int(input(f"You have {n} keychain. How many to remove : "))
        rem1=n-rem
        print(f"Now you have {rem1} keychain")
        return rem1
def vieworder():
        print(f"You have {n} keychain.")
        print("keychains cost $10 each")
        total=10*n
        print(f"total cost is ${total}")
        return total
def checkout(choose,total):
        print("CHECKOUT")
        name=input("what is your name? ")
        print(f"you have {choose} keychains")
        print("keychains cost $10 each")
        print(f"total cost is {total}")
        print(f"thank you for your order {name}")
n=0
while True:
    print("Ye olde keychain shoppe\n\n1. Add keychain to order\n2. Remove keychains from order\n3. View current order\n4. Checkout\n")
    print("\n")
    choose=(int(input("Please enter your choice : ")))
    if choose==1:
            n=addkeychains()         
    elif choose==2:
            n=removekeychain()
    elif choose==3:
            n=vieworder()
    elif choose==4:
                checkout(choose,n)
                break