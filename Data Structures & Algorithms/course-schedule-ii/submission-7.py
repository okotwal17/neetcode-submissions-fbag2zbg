class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = defaultdict(list)
        for p1, p2 in prerequisites:
            adjList[p1].append(p2)
        visited = set()
        seen = set()
        res = []
        def dfs(n):
            if n in visited:
                return True
            if n in seen:
                return False
            seen.add(n)
            for node in adjList[n]:
                if not dfs(node):
                    return False
            seen.remove(n)
            adjList[n] = []
            visited.add(n)
            res.append(n)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return []
        return res
        
        

            