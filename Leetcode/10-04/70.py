# Climbing Stairs
# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# Example 1:

# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# Example 2:

# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step

# Brute force solution would be to use a recursive approach (DFS)to calculate the number of ways to climb to the top.
# Time complexity: O(2^n) and space complexity: O(1).

# Optimal solution would be to use a dynamic programming approach to store the number of ways to climb to the top.
# Time complexity: O(n) and space complexity: O(n).
# Pattern:

class Solution:
    def climbStairs(self, n: int) -> int:
        one,two = 1,1
        
        for i in range(n-1):
            temp = one
            one = one + two
            two = temp
        return one
