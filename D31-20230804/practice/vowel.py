sentence="MY mind is not in static possition whatever may be god will help us"
split=sentence.split()
new=""
num=0
for i in split:
    strlen=len(i)
    if strlen>num:
        new=i
print(new)