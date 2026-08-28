# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        curr = slow
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        
        rev_curr = prev
        curr = head
        
        while curr and rev_curr:
            if curr.val != rev_curr.val:
                return False
            curr = curr.next
            rev_curr = rev_curr.next
        
        return True