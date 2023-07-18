data=[{"name":"sree","age":20,"place":"North thamaraikulam"},
      {"name":"ram","age":22,"place":"Putheri"},
      {"name":"siva","age":20,"place":"nagercoil"}]

def detail(data):
    for data1 in data:
        print("I am",data1["name"],"I am",data1["age"],"years old and I am from",data1["place"])
detail(data)

def age(data):
    for data1 in data:
        if data1["age"]>21:
            print(f"I am",data1["name"],"I am",data1["age"],"years old and I am from",data1["place"])
age(data)