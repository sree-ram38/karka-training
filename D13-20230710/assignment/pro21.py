height=float(input("Your height in m: "))
weight=int(input("Your weight in kg: "))
bmi=weight/height
if bmi<18.5:
    category="under weight"
elif bmi>=18.5 and bmi<=24.9:
    category="normal weight"
elif bmi>=25.0 and bmi<=29.9:
    category="overweight"
elif bmi>30.0:
    category="obese"

print(f"Your BMI is {bmi}\nBMI Category:{category}")