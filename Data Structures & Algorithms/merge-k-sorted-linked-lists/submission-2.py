# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge(list1, list2):
            dummy = merged = ListNode()
            curr1, curr2 = list1, list2
            while curr1 and curr2:
                if curr1.val <= curr2.val:
                    merged.next = curr1
                    curr1 = curr1.next
                else:
                    merged.next = curr2
                    curr2 = curr2.next
                merged = merged.next
            
            merged.next = curr1 if curr1 else curr2
            return dummy.next
        
        if not lists:
            return None
        
        merged_lsts = lists[:]
        while len(merged_lsts) > 1:
            next_lsts = []
            for i in range(0, len(merged_lsts), 2):
                first = merged_lsts[i]
                second = merged_lsts[i + 1] if i + 1 < len(merged_lsts) else None
                next_lsts.append(merge(first, second))
            merged_lsts = next_lsts
        
        return merged_lsts[0]
        
                
