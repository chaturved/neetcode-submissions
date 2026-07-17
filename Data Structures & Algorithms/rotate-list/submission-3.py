# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
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

        def reverse(node):
            prev = None
            while node:
                node.next, prev, node = prev, node, node.next
            return prev

        reverse_head = reverse(head)

        prev, curr = None, reverse_head
        for _ in range(k):
            curr.next, prev, curr = prev, curr, curr.next
        
        first_half = prev
        second_half = reverse(curr)

        reverse_head.next = second_half
        return first_half
     


