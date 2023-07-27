a=int(input("enter the number : "))
b=int(input("enter the number : "))
c=int(input("enter the number : "))

# if a>b:
#     print("largest number",a)
# elif a>c:
#     print("largest number",a)
# elif b>a:
#     print("largest number",b)
# elif b>c:
#     print("largest number",b)
# elif c>a:
#     print("largest number",c)
# elif c>b:
#     print("largest number",c)

if a>b:
    print(a)
    if a>c:
        print("largest number",a)
    else:
        print("largest number",c)
elif b>c:
    print("largest number",b)
else:
    print("largest number",c)