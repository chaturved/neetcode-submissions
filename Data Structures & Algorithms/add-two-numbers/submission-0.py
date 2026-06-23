# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        1 -> 2 -> 3 -> 7 -> 8 = 87321
        4 -> 5 -> 6 = 654
        87321 + 654
        """
        dummy = curr = ListNode()
        left, right = l1, l2
        carry = 0
        while left and right:
            summ = left.val + right.val + carry
            digit, carry = summ % 10, summ // 10
            curr.next = ListNode(digit)
            left, right, curr = left.next, right.next, curr.next
        
        while left:
            summ = left.val + carry
            digit, carry = summ % 10, summ // 10
            curr.next = ListNode(digit)
            left, curr = left.next, curr.next
        
        while right:
            summ = right.val + carry
            digit, carry = summ % 10, summ // 10
            curr.next = ListNode(digit)
            right, curr = right.next, curr.next
        
        if carry == 1:
            curr.next = ListNode(carry)

        return dummy.next