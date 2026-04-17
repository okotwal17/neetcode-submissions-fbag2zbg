class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dj_sets = [-1] * n
        def find(node):
            if dj_sets[node] < 0:
                return node
            dj_sets[node] = find(dj_sets[node])
            return dj_sets[node]
        def union(n1, n2):
            n1, n2 = find(n1), find(n2)
            if n1 == n2:
                return 0
            new_size = (dj_sets[n1] + dj_sets[n2])
            if dj_sets[n1] * -1 < dj_sets[n2] * -1:
                dj_sets[n1] = n2
                dj_sets[n2] = new_size
            else:
                dj_sets[n2] = n1
                dj_sets[n1] = new_size
            return 1
        res = n
        for v1, v2 in edges:
            res-=union(v1, v2)
        return res
