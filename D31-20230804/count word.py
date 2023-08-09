sen ="the quick brown fox jumps over the lazy dog the quick brown fox"

def many(sen):
    dictionary={}
    fun = sen.split()
    for data in fun:
        if data in dictionary:
            dictionary[data]=dictionary[data]+1
        else:
            dictionary[data]=1
        return dictionary
tot=many(sen)
print(tot)

# print("Pairs\n" + str(list(zip(fun, dictionary))))

# def many():
#     for data in sen:
# 	    if data in dictionary:
# 		    dictionary[data]+=1
#         else:
# 		dictionary[data]=1
# print("Count of all characters :\n "+ str(dictionary))

