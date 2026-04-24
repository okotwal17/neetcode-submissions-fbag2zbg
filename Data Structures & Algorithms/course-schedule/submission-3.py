class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjacencyList = {i : [] for i in range(numCourses)}
        for c1, c2 in prerequisites:
            adjacencyList[c1].append(c2)
        visited = set();
        def dfs(crs):
            if crs in visited:
                return False
            if len(adjacencyList[crs]) == 0:
                return True
            visited.add(crs)
            for c in adjacencyList[crs]:
                if not dfs(c):
                    return False
            visited.remove(crs)
            adjacencyList[crs] = []
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
