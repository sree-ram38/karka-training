def eligible(age):
    if age>=18:
        return "eligible"
    else:
        return "not eligible"

year=int(input("Enter your age :"))
result=eligible(year)
print(result)