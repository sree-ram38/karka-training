player=[{"country":"australia","name":"pat cummins","century":0,"half century":0,"wicket taken":124,"hat trick wicket":6,"top batting score":90},
        {"country":"sri lanka","name":"kumar sangakara","century":25,"half century":93,"wicket taken":0,"hat trick wicket":0,"top batting score":160},
        {"country":"india","name":"dhoni","century":46,"half century":65,"wicket taken":4,"hat trick wicket":0,"top batting score":183},
        {"country":"afghanisthan","name":"rashid khan","century":0,"half century":5,"wicket taken":167,"hat trick wicket":5,"top batting score":120},
        {"country":"west indies","name":"jason","century":0,"half century":12,"wicket taken":159,"hat trick wicket":4,"top batting score":110}]
def century(player):
    print("century players : ")
    for data in player:
        if data["century"]>10:
            print(data["name"])
          
def hat(player):
    print("Hat trick player : ")
    for data in player:
        if data["hat trick wicket"]>=5:
            print(data["name"])


def top(player):
    print("Top player")
    bat=0
    for data in player:
        if bat>data["top batting score"]:
            bat=data
            print(data["name"])

century(player)
print("\n")
hat(player)
print("\n")
top(player)