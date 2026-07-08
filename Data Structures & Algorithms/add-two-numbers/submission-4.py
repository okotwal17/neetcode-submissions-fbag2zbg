# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        p1, p2 = l1, l2
        cur = dummy
        carry = 0
        while p1 or p2 or carry:
            v1 = p1.val if p1 else 0
            v2 = p2.val if p2 else 0

            #new digit
            curVal = carry + v1 + v2
            carry = curVal //10
            curVal %= 10
            node = ListNode(curVal)
            cur.next = node

            #Update ptrs
            p1 = p1.next if p1 else None
            p2 = p2.next if p2 else None
            cur = cur.next
            
        return dummy.next