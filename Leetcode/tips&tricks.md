08-28:
    1.py - 2 Sum - Use hashmap to figure out if difference in array 
    49.py - Group Anagrams - Use hashmap to store the sorted string as the key and the list of anagrams as the value. Have to compare with ascii values to find and store hashmap of the characters
    217.py - Contains Duplicate - Use hashshet
    242.py - Valid Anagram - Cheatcode: sort strings and return true if same. use hashmap to store frequency of characters in strings, then compare

08-29:
    128.py - Longest Consecutive Sequence - use a hashset to store the elements of the array and then iterate through the array and check if the next element is in the hashset, check to see if element if start of sequence
   
    238.py - Product of Array Except Self - prefix and postfix 
    347.py - Top K Frequent Elements - imagine an array of size nums + 1 and let the frequency of each element in the index of the array. and the values at each index is a list of elements with that frequency. then, we can iterate through the array from the end and return the top k elements.

08-30:
    15.py - 3 Sum - 
    125.py - Valid Palindrome - Cheat: reverse string and compare, use 2 pointers (keep track of alphanumeric or not)
    167.py - 2 Sum II - 
    
    271.py - Encode and Decode Strings - use an integer to represent the length of the string and then a delimiter to announce start of the string itself.

09-02:
    53.py - Maximum Subarray - Remove negative prefix of sum, sliding window and pointers
    152.py - Maximum Product Subarray - DP, keep track of current min and max, ignore 0, max can be positive or negative but cant be zero
    371.py - Sum of Two Integers - bit mani, XOR (a ^ b), add bit by bit, be mindful of carry, after adding, if carry is still 1, then add it as well