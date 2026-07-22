class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        disjoint = [-1] * n
        def find(n):
            if disjoint[n] < 0:
                return n
            disjoint[n] = find(disjoint[n])
            return disjoint[n]
        def union(n1,n2):
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
            union(n1, n2)
        res = 0
        for n in disjoint:
            if n < 0:
                res += 1
        return res

                