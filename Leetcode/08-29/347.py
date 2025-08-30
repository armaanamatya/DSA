## Top K Frequent Elements

# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2

# Output: [1,2]

# Example 2:

# Input: nums = [1], k = 1

# Output: [1]

# Example 3:

# Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2

# Output: [1,2]

# Brute force solution would be to use a hashmap to store the frequency of each element and then sort the hashmap by frequency.
# Time complexity: O(nlogn) and space complexity: O(n).

# Optimal solution would be to use a heap to store the frequency of each element and then return the top k elements.
# Time complexity: O(nlogk) and space complexity: O(n).

# Instead lets use a bucket sort approach to store the frequency of each element and then return the top k elements.
# Time complexity: O(n) and space complexity: O(n).

# so, imagine an array of size nums + 1 and let the frequency of each element in the index of the array. and the values at each index is a list of elements with that frequency.

# then, we can iterate through the array from the end and return the top k elements.

from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        
        for n in nums:
            count[n] = 1 + count.get(n,0)
        
        for n, c in count.items():
            freq[c].append(n)
            
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
        
        return res