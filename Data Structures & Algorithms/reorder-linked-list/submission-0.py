class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        curr, slow.next = slow.next, None
        while curr:
            curr.next, prev, curr = prev, curr, curr.next

        left, right = head, prev
        while right:
            left.next, left = right, left.next
            right.next, right = left, right.next