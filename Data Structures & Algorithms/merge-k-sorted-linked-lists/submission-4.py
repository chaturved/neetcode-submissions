class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge(list1, list2):
            curr1, curr2 = list1, list2
            dummy = curr = ListNode()
            while curr1 and curr2:
                if curr1.val <= curr2.val:
                    curr.next = curr1
                    curr1 = curr1.next
                else:
                    curr.next = curr2
                    curr2 = curr2.next
                curr = curr.next

            if curr1:
                curr.next = curr1

            if curr2:
                curr.next = curr2

            return dummy.next

        def mergeK(lists):
            if len(lists) == 0:
                return None

            if len(lists) == 1:
                return lists[0]

            res = []
            for i in range(0, len(lists), 2):
                if i + 1 < len(lists):
                    res.append(merge(lists[i], lists[i + 1]))
                else:
                    res.append(lists[i])

            return mergeK(res)

        return mergeK(lists)