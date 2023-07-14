gender=input("What is your gender (M or F): ")
fname=input("First name: ")
lname=input("Last name: ")
age=int(input("Age :"))
print("\n")
martialstatus=input(f"Are you married {fname} (y or n)? ")
if gender=="M" and age>=20 and martialstatus=="Y":
    print(f"Then I shall call you Mr. {lname}")

elif gender=="M" and age<=20 and martialstatus=="N":
    print(f"Then I shall call you Mr. {lname}")

elif gender=="F" and age>=20 and martialstatus=="Y":
     print(f"Then I shall call you Mrs. {lname}")

elif gender=="F" and age<=20 and martialstatus=="N":
     print(f"Then I shall call you Ms. {lname}")

else:
     print("ERROR")