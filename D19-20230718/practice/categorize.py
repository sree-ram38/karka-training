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
    if val["category"]=="fruits":
        fruits["category"].append(val)
    else:
     vegetable["category"].append[val]
print(fruits)
print(vegetable)