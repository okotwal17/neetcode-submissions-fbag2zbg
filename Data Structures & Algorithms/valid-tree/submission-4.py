class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #Disjoint sets
        disjointSets = [-1] * n
        def find(n):
            if disjointSets[n] < 0:
                return n
            disjointSets[n] = find(disjointSets[n])
            return disjointSets[n]
        
        def union(n1, n2):
            n1, n2 = find(n1), find(n2)
            totalSize = disjointSets[n1] + disjointSets[n2]
            if n1 == n2:
                return False
            if disjointSets[n1] > disjointSets[n2]:
                disjointSets[n2] = totalSize
                disjointSets[n1] = n2
            else:
                disjointSets[n1] = totalSize
                disjointSets[n2] = n1
            return True

    
        
        for n1, n2 in edges:
            var = union(n1, n2)
            print(disjointSets, var)
            if not var:
                return False        
        
        res = 0
        for n in disjointSets:
            if n < 0:
                res += 1
            if res > 1:
                return False
        return True


