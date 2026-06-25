# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        group_prev = dummy
        group_head = head
        prev, curr = None, head
        count = 1

        while curr:
            curr.next, prev, curr = prev, curr, curr.next
            if count % k == 0:
                group_prev.next = prev
                group_prev = group_head
                group_head = curr
                prev = None
            count += 1
        
        if prev:
            curr, prev = prev, None
            while curr:
                curr.next, prev, curr = prev, curr, curr.next
            group_prev.next = group_head
        return dummy.next
