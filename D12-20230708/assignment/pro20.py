print("I will add up the numbers you give me ")
total=0
while True:
 
    number=int(input("Enter the number : "))
    total=number+total
    if total==0:
        break
    print(f"The total so far is : {total}")
    