# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        #Want a node after the group and want a node before the group
        #Start with a dummy node
        #Function to fetch for after. 
        dummy = ListNode(0, head)
        prevGroup = dummy
        cur = head        
        while True:
            #Where we are starting to reverse from
            startRev = self.getNthNode(prevGroup,k)
            #If theres not enough nodes to reverse, just link and break
            if not startRev:
                prevGroup.next = cur
                break
            postGroup = startRev.next
            #Initially, we are starting at startRev and we want endRev to end up at the end
            #This is where we reverse
            #3 --> 2 --> 1 4-->5-->6
            prev, cur2 = postGroup, cur
            while cur2 != postGroup:
                temp = cur2.next
                cur2.next = prev
                prev = cur2
                cur2 = temp
            #3 --> 2 --> 1 --> 4 -->5 -->6
            prevGroup.next = startRev
            cur.next = postGroup
            prevGroup = cur
            cur = postGroup
        return dummy.next

    def getNthNode(self,node, k):
        while node and k:
            node = node.next
            k -= 1
        return node