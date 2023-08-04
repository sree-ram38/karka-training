detail=[{"name":"sree",
        "email":"sreeram2003ic@gmail.com",
        "password":"sree87",
        "hobbies":["drawing","planting","hearing music"],
        "friend_list":["sree","abishek","aswin"]
        },
        {"name":"ram",
        "email":"ram123@gmail.com",
        "password":"ram87",
        "hobbies":["movie","cricket","ludo"],
        "friend_list":["najith","krishna","siva"]
        },
        {"name":"mithun",
        "email":"mithun21@gmail.com",
        "password":"fun@43",
        "hobbies":["drawing","planting","hearing music"],
        "friend_list":["sree","abishek","aswin"]
        }
        ]

user_email=input("Enter the email : ")
user_password=input("Enter the password : ")
for data in detail:
    email=data["email"]
    password=data["password"]
    if email==user_email and password==user_password:
            print("Your hobbies are : ",data["hobbies"])
            print("your friends are : ",data["friend_list"])
            
            
#             sudo apt update
# sudo apt install mysql-server
# sudo systemctl start mysql.service
# sudo mysql
# ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'sree2643';
# exit
# +
