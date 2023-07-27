data= [
    {"name": "Apple", "category": "Fruits"},
    {"name": "Carrot", "category": "Vegetables"},
    {"name": "Banana", "category": "Fruits"},
    {"name": "Broccoli", "category": "Vegetables"},
    {"name": "Strawberry", "category": "Fruits"},     
]
fruits=[]
vegetable=[]
for val in data:
    category = val["category"]
    name=val["name"]
    if val["category"]=="Fruits":
        fruits.append(name)
    else:
        vegetable.append(name)
print("Fruits : ",fruits)
print("Vegetables : ",vegetable)