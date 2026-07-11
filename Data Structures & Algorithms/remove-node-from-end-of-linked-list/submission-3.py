# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        p2, steps = head, n
        while p2:
            p2 = p2.next
            steps -= 1
            if not steps:
                break
        
        dummy = ListNode(-1, head)
        p1 = dummy
        while p2:
            p1 = p1.next
            p2 = p2.next
        p1.next = p1.next.next
        return dummy.next
        

