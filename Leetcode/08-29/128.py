# Longest Consecutive Sequence

# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

# Example 1:

# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
# Example 2:

# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9

# Brute force solution would be to use a hashset to store the elements of the array and then iterate through the array and check if the next element is in the hashset.
# or sort the array and then iterate through the array and check if the next element is consecutive.
# Time complexity: O(nlogn) and space complexity: O(n).

# Optimal solution would be to use a hashset to store the elements of the array and then iterate through the array and check if the next element is in the hashset.
# Time complexity: O(n) and space complexity: O(n).

from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0 
        
        for n in nums:
            # check if its the start of a sequence
            if (n - 1) not in numSet:
                length = 0
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)
        
        # length = 1
        # for n in numSet:
        #     if (n+1) in numSet:
        #         length += 1
        #     else:
        #         longest = max(length, longest)
        #         length = 1
        
        # longest = max(length, longest)
        
        return longest