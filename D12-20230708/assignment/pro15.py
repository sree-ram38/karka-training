print("TWO MORE QUESTIONS, BABY!\n\nThink of something and I'll try to guess it")
ques=input("QUESTION 1) Does it stay inside or outside or both? ")
ques1=input("QUESTION 2)Is it a living thing? ")

if ques=="inside" and ques1=="yes":
    print("It is a living thing, it is living in inside(houseplant)")
if ques=="outside" and ques1=="yes":
    print("It is a living thing which is living in the outside(bison)")
if ques=="both" and ques1=="yes":
    print("It will survive in both inside and outside(dog)")

if ques=="inside" and ques1=="no":
    print("It is a shower and curtain")
if ques=="outside" and ques1=="no":
    print("It is a billboard")
if ques=="both" and ques1=="no":
    print("It is a cell phone")