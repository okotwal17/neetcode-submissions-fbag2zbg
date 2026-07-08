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
            curVal = carry
            if p1:
                curVal += p1.val
            if p2:
                curVal += p2.val
            
            if curVal >=10:
                carry = curVal // 10
                curVal %= 10
            else:
                carry = 0
            node = ListNode(curVal)
            cur.next = node
            p1 = p1.next if p1 else None
            p2 = p2.next if p2 else None
            cur = cur.next
            
        return dummy.next