# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if(head is None):
            return head
        current = head
        length = 0
        while(current):
            length+=1
            current = current.next
        idx = length - n
        if(idx == 0):
            head = head.next
            return head
        currIdx = 0
        current = head
        while(currIdx < idx-1):
            currIdx+=1
            current = current.next
        current.next = current.next.next
        return head

        
        