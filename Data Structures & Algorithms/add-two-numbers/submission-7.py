# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        cur1, cur2 = l1, l2
        newList = dummy
        carry = 0
        while cur1 and cur2:
            value = cur1.val + cur2.val + carry
            if value >= 10:
                carry = 1
                value = value - 10
            else:
                carry = 0
            node = ListNode(value)
            newList.next = node
            newList = newList.next
            cur1 = cur1.next
            cur2 = cur2.next
        while cur1:
            value = cur1.val + carry
            if value >= 10:
                carry = 1
                value = value - 10
            else:
                carry = 0
            node = ListNode(value)
            newList.next = node
            newList = newList.next
            cur1 = cur1.next
        while cur2:
            value = cur2.val + carry
            if value >= 10:
                carry = 1
                value = value - 10
            else:
                carry = 0
            node = ListNode(value)
            newList.next = node
            newList = newList.next
            cur2 = cur2.next
        if carry:
            node = ListNode(1)
            newList.next = node
        return dummy.next
        