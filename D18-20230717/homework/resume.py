my_resume={"Name" :"SREERAM I",
            "E-mail":"sreeram2003ic@@gmail.com",
            "Mobile-No":9488217931,
            "Soft skills" : "coding",
            "Hard skills" : ["planting"],
            "Educational Qualification" :[{"SSLC-2018","S.M.Matric.Hr.Sec.School"},
                                          {"HSC-2020","S.M.Matric.Hr.Sec.School"},
                                          {"B.Sc-2023","S.T.Hindu.college"}],
            "Project" : "Android Development-compose input",
            "Experience":[{"company name":"amazon","role":"developer","duration":"3"},
                          {"company name":"clovion","role":"back end developer","duration":"2"},
                          {"company name":"TCS","role":"developer","duration":"4"},
                          ],
            "Hobbies" : ["planting","hearing music","drawing"],
            "Personal Details": {"Fathers name" :"IYYAPPAN",
                                 "Father's Occupation" :"mechanic",
                                 "Languages Known" :["Tamil","English"],
                                 "DOB" :"17-01-2003",
                                 "Genter":"Male",
                                 "Martial Status" :"Not Married",
                                 "Address" : {"Door No":"6/21",
                                              "Street Name" :"pillaiyaar kovil Street,North Thamarai kulam",
                                              "District" :"kanyakumari",
                                              "pin code": 629_704
                                             }
                                    } 
            }

for resume in my_resume["Hobbies"]:
    print(resume)
   
for lang in my_resume["Personal Details"]["Languages Known"]:
    print(lang)
   
for hard in my_resume["Hard skills"]:
    print(hard)
   
for edu in my_resume["Educational Qualification"]:
    print(edu)

for add in my_resume["Personal Details"]["Address"]["District"]:
    print(add)

# print(my_resume["Experience"])


