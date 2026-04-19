class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        sets = [-1] * n
        def find(node):
            if sets[node] < 0:
                return node
            sets[node] = find(sets[node])
            return sets[node]

        def union(n1, n2):
            n1, n2 = find(n1), find(n2)
            newSize = sets[n1] + sets[n2]
            if n1 == n2:
                return 0
            if sets[n1] < sets[n2]:
                sets[n2] = n1
                sets[n1] = newSize
            else:
                sets[n1] = n2
                sets[n2] = newSize
            return 1
        
        res = n
        for v1,v2 in edges:
            res-=union(v1,v2)
        return res

