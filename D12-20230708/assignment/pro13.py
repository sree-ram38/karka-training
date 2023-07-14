print("TWO QUESTIONS!\nThink of an object, and I'll try to guess it.\n")
ques=input("Question 1) Is it aniaml, vegetable, or mineral?\n>")
print("\n")
ques1=input("Question 2) Is it bigger than a breadbox?\n>")
print("\n")

if ques=="animal" and ques1=="yes":
    print("My guess is that you are thinking of a squirrel\nI would ask you If I'm right, but I don't actually care")
elif ques=="animal" and ques1=="no":
     print("My guess is that you are thinking of a moose\nI would ask you If I'm right, but I don't actually care")
elif ques=="mineral" and ques1=="yes":
    print("My guess is that you are thinking of a paper clip\nI would ask you If I'm right, but I don't actually care")
elif ques=="mineral" and ques1=="no":
    print("My guess is that you are thinking of a camaro\nI would ask you If I'm right, but I don't actually care")
elif ques=="vegetable" and ques1=="yes":
    print("My guess is that you are thinking of a carrot\nI would ask you If I'm right, but I don't actually care")
elif ques=="vegetable" and ques1=="no":
    print("My guess is that you are thinking of a watermelon\nI would ask you If I'm right, but I don't actually care")
else:
    print("ERROR")