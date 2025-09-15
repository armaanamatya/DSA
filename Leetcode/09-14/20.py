# Valid Parentheses

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Example 1:

# Input: s = "()"

# Output: true

# Example 2:

# Input: s = "()[]{}"

# Output: true

# Solution: Use a hashmap to store the close brackets and the corresponding open brackets. Use a stack to store the open brackets, and check if the close bracket is the same as the last open bracket.
# Time complexity: O(n) and space complexity: O(n).

class Solution:
    def isValid(self, s: str) -> bool:
        Map = {")": "(", "]": "[", "}": "{"}
        stack = []

        for c in s:
            if c in Map:
                # if the stack is not empty and the last element in the stack is the corresponding open bracket, then pop the last element
                if stack and stack[-1] == Map[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
            # add as many open brackets to the stack as possible
        return not stack