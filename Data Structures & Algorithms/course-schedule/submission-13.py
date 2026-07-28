class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = defaultdict(list)
        for p1, p2 in prerequisites:
            adjList[p1].append(p2)
        visited = set()
        def dfs(n):
            if n in visited:
                return False
            visited.add(n)
            for node in adjList[n]:
                if not dfs(node):
                    return False
            visited.remove(n)
            adjList[n] = []
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True