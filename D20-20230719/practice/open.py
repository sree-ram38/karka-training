# name=open("/home/sreeram/txt/name.txt","w")
# for data in name:
#     print(data)

# data=name.read()
# print(data)

# name.write("SREERAMGR")
# name.close()

# name=open("/home/sreeram/txt/name.txt","r")
# add=name.read()
# print(add)
# print(name.read(4))

name=open("/home/sreeram/txt/name.txt","a")
name.write("SREERAM \nAge : 20")
name.close()

name=open("/home/sreeram/txt/name.txt","r")
print(name.read())