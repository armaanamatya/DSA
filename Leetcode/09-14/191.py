# Number of 1 Bits

# Given a positive integer n, write a function that returns the number of set bits in its binary representation (also known as the Hamming weight).

# Example 1:

# Input: n = 11

# Output: 3

# Explanation:

# The input binary string 1011 has a total of three set bits.

# Example 2:

# Input: n = 128

# Output: 1

# Explanation:

# The input binary string 10000000 has a total of one set bit.

# Time complexity: O(1) and space complexity: O(1).
# Solution 1: Bitwise operations
class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        
        while n: # n != 0
            if n % 2: # to know if remainder/last bit is 1
                res += 1
            n = n >> 1 # to shift the number to the right by 1 bit [right shift operator]
        return res
    
# class Solution:
#     def hammingWeight(self, n: int) -> int:
#         res = 0
        
#         while n:
#             res += n % 2
#             n = n >> 1
#         return res

# Solution 2: Built-in function (Brian Kernighan's algorithm) (doing bitwise AND with n and n - 1 then incrementing the result until n is 0)
class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        
        while n:
            n = n & (n - 1)
            res += 1
        return res
    
# Time complexity: O(1) and space complexity: O(1).