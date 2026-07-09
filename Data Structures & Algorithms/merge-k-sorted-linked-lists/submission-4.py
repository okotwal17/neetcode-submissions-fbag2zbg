# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        #Adding to the
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
                heapq.heappush(heap, (lists[idx].val, idx, lists[idx]))
                lists[idx] = lists[idx].next
        return dummy.next
