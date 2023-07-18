mark=[
        {
            "name":"sree",
            "place":"North Thamaraikulam",
            "Hobbies":"drawing,planting",
            "sslc":{"tamil":60,
                    "english":60,
                    "maths":98,
                    "science":55,
                    "social science":78
                    }
         }
    ]


for marks in mark:
    total= sum(marks["sslc"].values())
    percentage=total/len(marks["sslc"].values())
    print(percentage)

    if percentage>90:
        print("you are eligible for maths-bio")
    elif percentage>85 and percentage<90:
        print("you are eligible for computer science")
    elif percentage>75 and marks["sslc"]["maths"]>=98:
        print("you are eligible for maths-bio in")
    elif percentage>=70 and marks["sslc"]["maths"]>=98:
        print("You are eligible for computer science")
