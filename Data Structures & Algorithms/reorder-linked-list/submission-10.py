# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        while fast:
            prev = slow
            slow = slow.next
            fast = fast.next
            if not fast:
                break
            fast = fast.next
        prev.next = None
        cur, prev = slow, None
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        cur1, cur2 = head, prev
        while cur1 and cur2:
            temp1, temp2 = cur1.next, cur2.next
            cur1.next = cur2
            cur2.next = temp1
            cur1 = temp1
            cur2 = temp2
