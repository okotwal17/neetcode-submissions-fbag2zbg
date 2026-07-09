# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        cur1 = dummy
        cur2 = head
        def getKthNode(node, k):
            k -= 1
            while node and k:
                node = node.next
                k -= 1
            return node
        while True:
            kthNode = getKthNode(cur2, k)
            if not kthNode:
                break
            print(kthNode.val)
            groupPrev = cur1
            groupNext = kthNode.next
            prev, cur = groupNext, cur2
            #Standard linked list reversal
            while cur != groupNext:
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp
            groupPrev.next = kthNode
            cur1 = cur2
            print(prev.val)
            cur2 = groupNext



        return dummy.next
        