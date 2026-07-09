# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        #Adding to the heap
        for i,node in enumerate(lists):
            if lists[i]:
                heapq.heappush(heap, (node.val, i, node))
                lists[i] = lists[i].next
        dummy = ListNode(-1)
        cur = dummy
        while heap:
            val, idx, node = heapq.heappop(heap)
            cur.next = node
            cur = cur.next
            if node.next:
                heapq.heappush(heap, (node.next.val, idx, node.next))
        return dummy.next
