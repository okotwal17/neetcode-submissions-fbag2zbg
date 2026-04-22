class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        sets = [-1] * n
        def find(node):
            if sets[node] < 0:
                return node
            sets[node] = find(sets[node])
            return sets[node]
        def union(n1, n2):
            n1, n2 = find(n1), find(n2)
            if n1 == n2:
                return False
            totalSize = sets[n1] + sets[n2]
            if sets[n1] < sets[n2]:
                sets[n2] = n1
                sets[n1] = totalSize
            else:
                sets[n1] = n2
                sets[n2] = totalSize
            return True
        def size(node):
            return sets[find(node)] * -1
        for v1, v2 in edges:
            if not union(v1, v2):
                return False
        if size(0) != n:
            return False
        return True