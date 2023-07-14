head=("WELCOME TO MECHELL'S TINY ADVENTURE!")
print(head)
ques=input("You are in a creepy house!  Would you like to go upstairs or into the kitchen? \n>")
ques1=input("There is a long curtentop with dirty dishes everywhere, off to one side\nThere is, as you'd expect, a refridgerator, You may open the refridgerator\nor look in a cabinet\n>")
ques2=input("Inside the refridgerator you see food and stuff. It look pretty nasty.\nwould you like to eat some of the food? (yes or no)\n>")
if ques=="kitchen" and ques1=="refridgerator" and ques2=="no":
    print("You die of starvation......... Eventually")
elif ques=="kitchen" and ques1=="refridgerator" and ques2=="yes":
    print("You will die of starvation")
if ques=="upstairs" and ques1=="To room" and ques2=="no":
        print("Then go to sleep")
elif ques=="upstairs" and ques1=="To room" and ques2=="yes":
        print("Then go to kitchen")