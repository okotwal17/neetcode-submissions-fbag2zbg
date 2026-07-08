# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #If len <= 1, just return early
        if not head or not head.next:
            return
        #Have before the point of reversal, point of reversal, and fast pointer
        prev, slow, fast = None,head, head
        while fast:
            prev = slow
            slow = slow.next
            fast = fast.next
            if not fast:
                break
            fast = fast.next
        #Before point of reversal, set to null
        prev.next = None
        prev, curr = None, slow
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        #Prev is our "pointer" on the right
        #p1 is left pointer, p2 is right pointer
        p1, p2 = head, prev
        while p1 and p2:
            nextP1, nextP2 = p1.next, p2.next
            p1.next = p2
            p2.next = nextP1
            p1, p2 = nextP1, nextP2


            
        
        
