# a function to find area of a triangle using Heron’s formula.

def triangle():
    area=(sp*(sp-l1)*(sp-l2)*(sp-l3)) ** 0.5
    l1=int(input("Enter the value of length1 : "))
    l2=int(input("Enter the value of lenth2 : "))
    l3=int(input("Enter the value of length3 : "))
    sp=l1+l2+l3/2
    return area
# print(triangle(l1,l2,l3,sp))


# Function to find area of a Square
def square():
    side=int(input("Enter the value : "))
    return side*side
# print(square(side))

# Function to find area of a rectangle
def rect():
    len=int(input("Enter the value of length : "))
    wid=int(input("Enter the value of width : "))
    return len*wid
# print(rect(len,wid))


# Function to find area of a Circle.
def circ():
   rad=int(input("Enter the value of radius : "))
   return (3.14)*rad*rad
# print(circ(rad))

# function to find trapezium
def trapezium():
    b1=int(input("Enter the value of base1 : "))
    b2=int(input("Enter the value of base2 : "))
    height=int(input("Enter the value of height : "))
    return (b1+b2)/2*height
# print(trapezium(b1,b2,height))


choice=int(input("Enter the function choice : "))
if choice==1:
    print(triangle())
elif choice==2:
    print(square())
elif choice==3:
    print(rect())
elif choice==4:
    print(circ())
elif choice==5:
    print(trapezium())