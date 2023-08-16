# Longest Substring Without Repeating Characters Given a string s, find the length of the longest substring without repeating characters. 
# Input: s = "abcabcbb" 
# Output: 3 
# Explanation: The answer is "abc", with the length of 3.



s="abcabcbb"
em=""
for i in s:
    if i not in em:
        em=em+i
print(f"the ans is {em},with the length{len(em)}")