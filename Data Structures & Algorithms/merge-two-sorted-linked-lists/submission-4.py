# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l, r = list1, list2
        dummy = ListNode()
        curr = dummy
        while l and r:
            if l.val > r.val:
                curr.next = r
                curr = curr.next
                r = r.next
            else:
                curr.next = l
                curr = curr.next
                l = l.next
        curr.next = r if not l else l
        return dummy.next
            