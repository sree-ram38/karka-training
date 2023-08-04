a=0    
b=1    
value=int(input("Enter the value : "))
for i in range(0,value):  
    print(a)
    c=a+b
    a=b 
    b=c 



# def fibonacci(n):
#   if n == 0:
#     return 0
#   elif n == 1:
#     return 1
#   else:
#     return fibonacci(n-1) + fibonacci(n-2)

# # Generate the first 10 numbers in the Fibonacci series
# for i in range(10):
#   print(fibonacci(i))



# def fibonacci(n):
#   a, b = 0, 1
#   for i in range(n):
#     a, b = b, a+b
#   return a
# # Generate the first ten numbers in the Fibonacci series
# for i in range(10):
#   print(fibonacci(i))


# def fibonacci(n):
#   a, b = 0, 1
#   result = []
#   for i in range(n):
#     result.append(a)
#     a, b = b, a+b
#   return result
# # Generate the first ten numbers in the Fibonacci series
# print(fibonacci(10))






# define a function to generate the Fibonacci series
# def fibonacci(n):
# base case: the first two numbers in the series are 1
#   if n == 1 or n == 2:
#     return 1
# recursive case: the next number is the sum of the previous two
#   return fibonacci(n-1) + fibonacci(n-2)

# prompt the user for the number of terms to generate
# num_terms = int(input("Enter the number of terms to generate: "))

# generate and print the Fibonacci series
# for i in range(1, num_terms+1):
#   print(fibonacci(i), end=" ")





# a=0
# while 0:
#     a=a+1
#     print(a)