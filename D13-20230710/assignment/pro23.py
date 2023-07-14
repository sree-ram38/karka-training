num=range(1,101)
for i in num:
    if i%3==0 and i%5==0 :
        print(i,"FizzBuzz")
    elif i%5==0:
        print(i,"Buzz")
    elif i%3==0 :
        print(i,"Fizz")