# Missing Number

# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

# Example 1:

# Input: nums = [3,0,1]

# Output: 2

# Explanation:

# n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.

# Example 2:

# Input: nums = [0,1]

# Output: 2

# Explanation:

# n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.

# Simple solution would be to use a hashset to store the elements of the array and then iterate through the range [0, n] and check if the element is in the hashset.
# Time complexity: O(n) and space complexity: O(n).

from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        hashSet = set(nums)
        for i in range(len(nums) + 1):
            if i not in hashSet:
                return i
        return -1
    
# Optimal solution would be to use the formula for the sum of the first n natural numbers.
# Time complexity: O(n) and space complexity: O(1).

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return sum(range(len(nums) + 1)) - sum(nums)
    
# Solution 2: Bitwise XOR
# Time complexity: O(n) and space complexity: O(1).

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums) + 1):
            res ^= i
        for n in nums:
            res ^= n
        return res
    