# Encode and Decode Strings

# Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

# Please implement encode and decode

# Example 1:

# Input: ["neet","code","love","you"]
#--> encoded = "neetcodeloveyou"
# Output:["neet","code","love","you"]
# --> decoded = ["neet","code","love","you"]
# Example 2:

# Input: ["we","say",":","yes"]
# --> encoded = "wesay:yes"
# Output: ["we","say",":","yes"]
# --> decoded = ["we","say",":","yes"]
# You should aim for a solution with O(m) time for each encode() and decode() call and O(m+n) space, where m is the sum of lengths of all the strings and n is the number of strings.

# You should aim for a solution with O(m) time for each encode() and decode() call and O(m+n) space,
# where m is the sum of lengths of all the strings and n is the number of strings.

# Optimal solution would be to use an integer to represent the length of the string and then a delimiter to announce start of the string itself.

from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res
    
    def decode(self, s: str) -> List[str]: 
        res = []
        i = 0
        
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            
            length = int(s[i:j])
            
            res.append(s[j+1 : j+1 + length])
            i = j + 1 + length 
            
        return res