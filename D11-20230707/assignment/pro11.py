wei=int(input("Please enter your current earth weight:"))
print("\n")
a=("I have information for the following planets:\n\t1. venus\t2 .Mars\t\t3. Jupiter\n\t4. Saturn\t5. Uranus\t6. Neptune\n")
print(a)
planet=int(input("Which planet are you visiting :"))

if planet==1:
    planets=wei*0.78
    
elif planet==2:
    planets=wei*0.39

elif planet==3:
    planets=wei*2.65

elif planet==4:
    planets=wei*1.17

elif planet==5:
    planets=wei*1.05
    
elif planet==6:
    planets=wei*1.23

print(f"Your weight would be {planets} pounds on that planet")