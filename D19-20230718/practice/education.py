education=[{"studied":"B.Tech","Institute":"cape","semester mark":
            [
            {
            "semester name":1,
            "subject":["computer programming","maths","data science"],
            "semester grade":"A"
            }
            ]
            }
            [{
            "semester name":2,
            "subject":["Digital image processing","science","python"],
            "semester grade":"B"             
            }]
            [{
            "semester name":3,
            "subject":["Machine learning","botany","c programming"],
            "semester grade":"A"               
            }]
            [{
            "semester name":4,
            "subject":["IOT","graphics","environmental science"],
            "semester grade":"A"               
            }]
            [{
            "semester name":5,
            "subject":["My SQL","maths","computer architecture"],
            "semester grade":"A"                
            }]
            [{
            "semester name":6,
            "subject":["data structure","maths","software engineering"],
            "semester grade":"B"                
            }]
            ]
for data in education:
    print(data["studied"])