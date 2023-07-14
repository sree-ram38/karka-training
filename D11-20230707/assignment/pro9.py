day=int(input("Enter the date :"))
if day==1:
    print("Today is a sunday")
elif day==2:
    print("Today is a monday")
elif day==3:
    print("Today is a tuesday")
elif day==4:
    print("Today is a wednesday")
elif day==5:
    print("Today is a thursday")
elif day==6:
    print("Today is a friday")
elif day==7 or day==0:
    print("Today is a saturday")
else:
    print("error")