# Implement a Python function to find the longest common prefix among a list of strings. 
# Example:
#  Output: "fl”
# List: ["flower", "flow", "flight"]

# def longestCommonPrefix(self, strs: List[str]) -> str:
#     res = ""
#     for a in zip(*strs):
#         if len(set(a)) == 1: 
#             res += a[0]
#         else: 
#             return res
#     return res
                        
# longestCommonPrefix()



list=["flower", "flow", "flight"]
max=0
min=len(list[0])
output=""
# print(min)
arg=sorted(list)
for word in arg:
    num=len(word)
    # print(num)
    if num>max:
        max=num
        ans1=word
    if num<min:
        min=num
        ans2=word
for i in range(len(ans2)):
    if ans1[i]==ans2[i]:
        output+=ans1[i]
print("longest common letter :",output)