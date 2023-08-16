# value=[3,4,5,7,4,3]
# for data in range(len(value)):
#     count=0
#     for j in range(len(value)):
#         if value[data]==value[j]:
#             count+=1
#     if count==1:
# 	    print(value[data])
            
# ar = [2, 3, 5, 4, 5, 3, 4]
# n = len(ar)
# def findSingle(A, ar_size)
# 	for i in range(ar_size):
# 		count = 0
# 		for j in range(ar_size):
# 			if(A[i] == A[j]):
# 				count += 1
# 		if(count == 1):
# 			return A[i]
# 	return -1
# print("Element occurring once is", findSingle(ar, n))


# value=[3,4,5,7,4,3]
# empty=[]
# for data in range(len(value),-1):
#     a=value[data]==data
#     empty.append(a) 
# print(empty)


list=[1,2,2,3]
dic={}
for i in list:
    if i not in dic:
     dic[i]=1
    else:
     dic[i]=dic[i]+1  
  
for j in dic:
  if dic[j]==1:
   print(j)