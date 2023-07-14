i1=int(input("Enter the value of i1="))
i2=int(input("Enter the value of i2="))
i3=int(input("Enter the value of i3="))
i4=int(input("Enter the value of i4="))
total=i1+i2+i3+i4
print(total)
if (total>=500)and(total<=1000):
    print("You have won a silver token")
elif total>=1000:
    print("You have won a gold token")
else:
    print("You have not won a token")