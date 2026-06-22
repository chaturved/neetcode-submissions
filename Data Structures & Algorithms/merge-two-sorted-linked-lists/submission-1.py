# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        
        if not list2:
            return list1

        left_curr = list1
        right_curr = list2
        dummy = new_curr = ListNode()

        while left_curr and right_curr:
            if left_curr.val <= right_curr.val:
                new_curr.next = left_curr
                left_curr = left_curr.next
            else:
                new_curr.next = right_curr
                right_curr = right_curr.next
            
            new_curr = new_curr.next
        
        new_curr.next = left_curr or right_curr
        return dummy.next