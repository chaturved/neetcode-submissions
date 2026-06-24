# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
            dummy = merged = ListNode()
            curr1 = list1
            curr2 = list2
            while curr1 and curr2:
                if curr1.val <= curr2.val:
                    merged.next = curr1
                    curr1 = curr1.next
                else:
                    merged.next = curr2
                    curr2 = curr2.next
                merged = merged.next
            
            if not curr1:
                merged.next = curr2
            
            if not curr2:
                merged.next = curr1
            
            return dummy.next
        
        head = None
        for curr in lists:
            head = merge(head, curr)
        
        return head
                
