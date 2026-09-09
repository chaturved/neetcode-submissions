# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        curr = head
        dummy_head = ListNode()
        dummy = dummy_head
        while curr:
            if curr.val != val:
                dummy.next = curr
                dummy = dummy.next
            curr = curr.next
        
        dummy.next = None
        return dummy_head.next