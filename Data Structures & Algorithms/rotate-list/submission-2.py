# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        6 -> 5 -> 4 -> 3 -> 2 -> 1

        6 <- 5 <- 4 [4, 5, 6]
        3 <- 2 <- 1 [1, 2, 3]

        connect 6 to 1
        """
        if not head:
            return None
        curr = head
        n = 0
        while curr:
            curr = curr.next
            n += 1

        k = k % n
        if k == 0:
            return head

        prev, curr = None, head
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        
        reverse_head = prev
        prev, curr = None, prev
        for _ in range(k):
            curr.next, prev, curr = prev, curr, curr.next
        
        first_half = prev
        prev, curr = None, curr
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        
        second_half = prev
        reverse_head.next = second_half
        return first_half


