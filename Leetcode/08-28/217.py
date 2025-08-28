## Contains Duplicate

# Given an integer array nums, return true if any value appears at least twice in the array, 
# and return false if every element is distinct.

# Example 1:

# Input: nums = [1,2,3,1]

# Output: true

# Explanation:

# The element 1 occurs at the indices 0 and 3.

# Example 2:

# Input: nums = [1,2,3,4]

# Output: false

# Explanation:

# All elements are distinct.

# So brute force solution of nested loops is time complexity: O(n^2) and since no extra memory space complexity: O(1).

# If sorted and then check: time complexity: O(nlogn) and space complexity: O(1).

# Optimal solution would be using a hashset to store the elements of the array.

# Time complexity: O(n) and space complexity: O(n).

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
    
    