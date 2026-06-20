# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        curNode = dummy
        while True:
            curMin, minNode, nodeIdx = float('inf'), None, -1
            for i in range(len(lists)):
                if lists[i] and lists[i].val < curMin:
                    curMin = lists[i].val
                    minNode = lists[i]
                    nodeIdx = i
            if curMin != float('inf'):
                curNode.next = minNode
                curNode = curNode.next
                lists[nodeIdx] = lists[nodeIdx].next
            else:
                break
        return dummy.next