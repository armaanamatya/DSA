# Counting Bits

# Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.
# Example 1:

# Input: n = 2
# Output: [0,1,1]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10

# Example 2:
# nput: n = 5
# Output: [0,1,1,2,1,2]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# 3 --> 11
# 4 --> 100
# 5 --> 101

#Brute force solution would be to integer mod first to get remainder(% mod 2) then integer divide by 2 to get the quotient(// divide) then increment the result by 1 for each 1 in the binary representation.
# Time complexity: O(nlogn) and space complexity: O(1).

# Optimal solution would be to use a dynamic programming approach to store the number of 1's in the binary representation of i.
# Time complexity: O(n) and space complexity: O(n).
# Pattern:
 
# 0 --> 0 = 0 
# 1 --> 1 = 1 + dp[n-1]
# 2 --> 10 = 1 + dp[n-2]
# 3 --> 11 = 1 + dp[n-2]
# 4 --> 100 = 1 + dp[n-4]
# 5 --> 101 = 1 + dp[n-4]
# 6 --> 110 = 1 + dp[n-4]
# 7 --> 111 = 1 + dp[n-4]
# 8 --> 1000 = 1 + dp[n-8]

# Most significant bit: is always a power of 2
# if i is a power of 2, then dp[i] = 1
# if i is not a power of 2, then dp[i] = dp[i-1] + 1

from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n+1)
        
        offset = 1
        for i in range(1, n+1):
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset]
        return dp
    