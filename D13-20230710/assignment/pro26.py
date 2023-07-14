# print("Ye olde keychain shoppe\n\n1. Add keychain to order\n2. Remove keychains from order\n3. View current order\n4. Checkout\n")

# print("\n")

# def add_keychains():
#     return "ADD KEYCHAINS"

# def remove_keychains():
#     return "REMOVE KEYCHAIN"

# def view_order():
#     return "VIEW ORDER"

# def checkout():
#     return "CHECKOUT"

# choice=int(input("Please enter your choice: "))
# print("\n")
# if choice==1:
#     print(add_keychains())
# elif choice==2:
#     print(remove_keychains())
# elif choice==3:
#     print(view_order())
# elif choice==4:
#     print(checkout())





def add_keychains():
    return "ADD KEYCHAINS"

def remove_keychains():
    return "REMOVE KEYCHAIN"

def view_order():
    return "VIEW ORDER"

def checkout():
    return "CHECKOUT"


for i in range(8):
    choice=int(input("Enter the choice : "))
    if choice==1:
        print(add_keychains())
    elif choice==2:
        print(remove_keychains())
    elif choice==3:
        print(view_order())
    elif choice==4:
        print(checkout())
        break