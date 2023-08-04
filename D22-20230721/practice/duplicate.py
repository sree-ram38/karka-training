
# val=["value"]
# print(dup_val)
# res=set(dup_val)
# print(res)
# res=dict(zip(dup_val,val))
# print(res)
# list(OrderedDict.fromkeys(dup_val).keys())
dup_val=[1,2,1,3,2,4,3,5,3,5,1,9,6,7]
original=[]
for dup in dup_val:
    if dup not in original:
        original.append(dup)
print("original value : ",original)