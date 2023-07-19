groups=[{"name" : "shiva", 
        "place":"kotter",
       "hobbeis" :["dance","music","drawing"],
        "marks":{"tamil":100,
                 "eng":88,
                 "maths":78,
                 "science" :99,
                 "social":100 }},
        {"name" : "abi",
        "place":"nagercoil",
       "hobbeis" :["dance","music","drawing"],
        "marks":{"tamil":100,
                 "eng":92,
                 "maths":100,
                 "science" :76,
                 "social":100}},
        {"name" : "gayathri",
        "place":"vadaseri",
       "hobbeis" :["dance","music","drawing"],
        "marks":{"tamil":50,
                 "eng":40,
                 "maths":100,
                 "science" :35,
                 "social":66}},     
         ]

for group in groups:
    # print(group)
    mark=(group["marks"])
    m1=mark["tamil"]
    m2=mark["eng"]
    m3=mark["maths"]
    m4=mark["science"]
    m5=mark["social"]
    tot=m1+m2+m3+m4+m5
    per=(tot*100)/500
    print(per)

    if per>90:
        print(group["name"],"Eligible for maths bio")
    elif per>80 and per<90:
        print(group["name"],"Eligible for computer science")
    elif per>75 and mark["maths"]<=98:
        print("Eligible for maths bio, the maths morethen 98")
    elif per>70 and mark["maths"]<=98: 
         print("Eligible for computer science , the maths morethen 98")  








    



                       