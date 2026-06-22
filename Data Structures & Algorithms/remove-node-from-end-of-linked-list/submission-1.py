# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        remove nth from end of list = length - n + 1
        1->2->3->4
        """

        length = 0
        curr = head
        while curr:
            curr = curr.next
            length += 1

        prev = None
        curr = head
        curr_n = 1

        while curr:
            if curr_n == length - n + 1:
                if prev:
                    prev.next = curr.next
                else:
                    head = head.next
            prev = curr
            curr = curr.next
            curr_n += 1
        
        return head