# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        prev, slow, fast = None, head, head
        #Find splitpoint
        while fast:
            prev = slow
            slow = slow.next
            fast = fast.next
            if not fast:
                break
            fast = fast.next
        #Break properly
        prev.next = None
        prev, cur = None, slow
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        #Prev is now head 
        p1, p2 = head, prev
        while p1 and p2:
            p1Next = p1.next
            p2Next = p2.next
            p1.next = p2
            p2.next = p1Next
            p1, p2 = p1Next, p2Next


