# Group Anagrams

# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]

# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Explanation:

# There is no string in strs that can be rearranged to form "bat".
# The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
# The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
# Example 2:

# Input: strs = [""]

# Output: [[""]]

# Brute force solution would be to sort each string and then use a hashmap to group the anagrams.
# Time complexity: O(m * nlogn) and space complexity: O(n). where m is the length of strs and n is the length of the longest string.

# Optimal solution would be to use a hashmap to store the sorted string as the key and the list of anagrams as the value.
# Time complexity: O(m * n) and space complexity: O(n). where m is the length of strs and n is the length of the longest string.

from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = defaultdict(list) # sorted string : list of anagrams
                     # mapping charCOunt to lsit of Anagrams
                     
        for s in strs:
            count = [0] * 26 # a ... z

            for c in s:
                count[ord(c) - ord("a")] += 1
                
            hashMap[tuple(count)].append(s)

        return hashMap.values()