ready=input("Are you ready for the quiz : ")
print("Okay, here it comes!")
n=0
print("Q1) What is the capital of Tamil Nadu?\n\t 1.Chennai\n\t 2.Mumbai\n\t 3.Bangalore\n\n\t")

q=input(">")
if q=="1":
    print("That's correct")
    n=n+1
else:
    print("That's not correct")

q1=input("Q2) Tea contains more caffeine than coffee and soda? \n\t1) Yes\n\t2) No\n\n>")
if q1=="1":
    print("That's correct")
    n=n+1
else:
    print("That's not correct")

q2=input("Q3) The absorption of ink by blotting paper involves\n\t1) viscosity of ink\n\t2) capillary action phenomenon\n\t3) siphon action\n\n>")
if q2=="2":
    print("That's correct")
    n=n+1
else:
    print("That's not correct")

print(f"Overall, you get {n} out of 3 correct \n Thanks for playing")