class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        sets = [-1] * len(edges)
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
        for v1, v2 in edges:
            if not union(v1 - 1, v2 - 1):
                return [v1,v2]
            print(sets)
        return [-1]
            