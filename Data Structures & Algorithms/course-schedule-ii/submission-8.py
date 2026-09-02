class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = defaultdict(list)
        for p1, p2 in prerequisites:
            adjList[p1].append(p2)
        visited = set()
        seen = set()
        res = []
        def dfs(p):
            if p in seen:
                return True
            if p in visited:
                return False
            visited.add(p)
            for c in adjList[p]:
                if not dfs(c):
                    return False
            visited.remove(p)
            res.append(p)
            seen.add(p)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return []
        return res