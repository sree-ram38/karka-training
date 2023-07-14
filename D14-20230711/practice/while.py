# i=2
# while i<12:
#     print(i)
#     i=i+1 



def add_keychains():
    return "ADD KEYCHAINS"

def remove_keychains():
    return "REMOVE KEYCHAIN"

def view_order():
    return "VIEW ORDER"

def checkout():
    return "CHECKOUT"

choice=int(input("Enter the choice : "))
while choice<=4:
   
    if choice==1:
        print(add_keychains())
    elif choice==2:
        print(remove_keychains())
    elif choice==3:
        print(view_order())
    elif choice==4:
        print(checkout())
        break