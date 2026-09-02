class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = defaultdict(list)
        for p1, p2 in prerequisites:
            adjList[p1].append(p2)
        visited = set()
        def dfs(p):
            if not adjList[p]:
                return True
            if p in visited:
                return False
            visited.add(p)
            for c in adjList[p]:
                if not dfs(c):
                    return False
            visited.remove(p)
            adjList[p] = []
            return True
        keys = adjList.keys()
        for p in list(keys):
            if not dfs(p):
                return False
        return True
        
