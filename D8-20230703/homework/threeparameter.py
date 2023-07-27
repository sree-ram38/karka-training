def para(first_number,operator,second_number):
    if operator=="+":
        return(first_number+second_number)
    elif operator=="-":
        return(first_number-second_number)
    elif operator=="*":
        return(first_number*second_number)
    elif operator=="/":
        return(first_number/second_number)
    elif operator=="%":
        return(first_number%second_number)
    elif operator=="**":
        return(first_number**second_number)

print("INPUT:")
first_number=int(input("Enter the first number :"))
operator=input("Enter the operator :")
second_number=int(input("Enter the second number :"))

print("RESULT:")
Answer=para(first_number,operator,second_number)
print("Answer =",Answer)