# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = merged = ListNode()

        curr_lst = [(head.val, i, head) for i, head in enumerate(lists) if head]
        heapq.heapify(curr_lst)

        while curr_lst:
            _, i, curr = heapq.heappop(curr_lst)
            merged.next = curr
            merged = merged.next
            if curr.next:
                heapq.heappush(curr_lst, (curr.next.val, i, curr.next))
        
        return dummy.next


