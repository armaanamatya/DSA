## Two Sum

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

# Brute force solution is nested loops. Time complexity: O(n^2) and space complexity: O(1).

# Optimal solution is using a hashmap to store the indices of the elements.

# Hashmap:
#  value : its index

# Time complexity: O(n) and space complexity: O(n).

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {} # val : index
        
        for i,n in enumerate(nums):
            diff = target - n
            if diff in hashMap:
                return [hashMap[diff], i]
            
            hashMap[n] = i
        return []