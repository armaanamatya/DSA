# Reverse Bits

# Reverse bits of a given 32 bits signed integer.

# Example 1:

# Input: n = 43261596

# Output: 964176192

# Explanation:

# Integer	Binary
# 43261596	00000010100101000001111010011100
# 964176192	00111001011110000010100101000000

# Solution 1: Bitwise operations
# Time complexity: O(1) and space complexity: O(1).

class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        
        for i in range(32):
            bit = (n >> i) & 1 # getting the bit at the ith position
            res = res | (bit << (31 - i)) # setting the bit at the 31 - i position (in the output)
        return res
            
# Solution 2: Bitwise operations
# Time complexity: O(1) and space complexity: O(1).

class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for _ in range(32):
            last_bit=n & 1 # getting the last bit
            n=n>>1 # shifting the number to the right by 1 bit
            result = (result<<1) | (last_bit) # shifting the result to the left by 1 bit and adding the last bit
        return result 