list=[100,200,300,100,250,558]
list1=0
def built(list,list1):
    for num in list:
        if list1>num:
            list1=num
    return num
    
print("output largest number :""\n",built(list,list1))