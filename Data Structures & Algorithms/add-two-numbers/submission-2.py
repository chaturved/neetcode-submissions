# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = curr = ListNode()
        left, right = l1, l2
        carry = 0

        while left or right:
            l_val = left.val if left else 0
            r_val = right.val if right else 0
            summ = l_val + r_val + carry
            digit, carry = summ % 10, summ // 10

            node = left if left else right
            node.val = digit
            curr.next = node

            left = left.next if left else None
            right = right.next if right else None
            curr = curr.next

        if carry:
            curr.next = ListNode(carry)

        return dummy.next