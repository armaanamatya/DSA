# Reverse Linked List

# Given the head of a singly linked list, reverse the list, and return the reversed list.
#Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?

# Input: head = [1,2,3,4,5] === 1-> 2-> 3-> 4-> 5-> None
# Output: [5,4,3,2,1] === 5-> 4-> 3-> 2-> 1-> None

# Brute force solution would be to use a recursive approach to reverse the list.
# Time complexity: O(n) and space complexity: O(n).
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head 
        head.next = None
        return newHead
    
# Optimal solution would be to use an iterative approach to reverse the list.
# Time complexity: O(n) and space complexity: O(1).

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev