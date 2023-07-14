leap=int(input("Enter the year :"))
if((leap%4==0) and (leap%100!=4))or(leap%400==0):
    print(leap,",it is a leap year")
else:
    print(leap,",it is not a leap year")