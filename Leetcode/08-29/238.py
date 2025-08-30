# Product of Array Except Self

# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]

# Brute force solution would be to use nested loops to calculate the product of all the elements except the current element.
# Time complexity: O(n^2) and space complexity: O(1).

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n
        
        # For each element, calculate product of all other elements
        for i in range(n):
            for j in range(n):
                # Skip the current element
                if i != j:
                    result[i] *= nums[j]
        
        return result

# Optimal solution would be to use prefix and postfix product (2 passes through the array).
# Time complexity: O(n) and space complexity: O(1) (not counting the result array).

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))
        # res = [1, 1, 1, 1] (initial) for nums = [1, 2, 3, 4]
        
        for i in range(1, len(nums)):
            res[i] = res[i-1] * nums[i-1]
        
        # Pass 1: Left-to-Right (Prefix Products)
        # i=1: res[1] = res[0] * nums[0] = 1 * 1 = 1 → res = [1, 1, 1, 1]
        # i=2: res[2] = res[1] * nums[1] = 1 * 2 = 2 → res = [1, 1, 2, 1]
        # i=3: res[3] = res[2] * nums[2] = 2 * 3 = 6 → res = [1, 1, 2, 6]
        # After pass 1: res[i] contains the product of all elements to the left of nums[i].
         
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
            
        # Pass 2: Right-to-Left (Suffix Products)
        # postfix = 1 (tracks product of elements to the right)
        # i=3: res[3] *= postfix = 6 * 1 = 6, then postfix *= nums[3] = 1 * 4 = 4 → res = [1, 1, 2, 6]
        # i=2: res[2] *= postfix = 2 * 4 = 8, then postfix *= nums[2] = 4 * 3 = 12 → res = [1, 1, 8, 6]
        # i=1: res[1] *= postfix = 1 * 12 = 12, then postfix *= nums[1] = 12 * 2 = 24 → res = [1, 12, 8, 6]
        # i=0: res[0] *= postfix = 1 * 24 = 24, then postfix *= nums[0] = 24 * 1 = 24 → res = [24, 12, 8, 6]   
        return res 