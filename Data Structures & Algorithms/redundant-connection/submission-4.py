class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        disjoint = [-1] * len(edges)
        def find(n):
            if disjoint[n] < 0:
                return n
            disjoint[n] = find(disjoint[n])
            return disjoint[n]
        def union(n1, n2):
            n1, n2 = find(n1), find(n2)
            if n1 == n2:
                return False
            totalSize = disjoint[n1] + disjoint[n2]
            if disjoint[n1] < disjoint[n2]:
                disjoint[n1] = totalSize
                disjoint[n2] = n1
            else:
                disjoint[n2] = totalSize
                disjoint[n1] = n2
            return True
        for n1, n2 in edges:
            if not union(n1 - 1, n2 - 1):
                return [n1, n2]

