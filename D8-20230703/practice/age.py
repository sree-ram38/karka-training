def eligible(age):
    if age>=18:
        return "eligible"
    else:
        return "not eligible"

age=int(input("Enter your age :"))
# result=eligible(age)
print(eligible(age))