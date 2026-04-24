class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjacencyList = {i : [] for i in range(numCourses)}
        for c1, c2 in prerequisites:
            adjacencyList[c1].append(c2)
        visited = set()
        cycle = set()
        path = []
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visited:
                return True
            cycle.add(crs)
            for c in adjacencyList[crs]:
                if not dfs(c):
                    return False
            path.append(crs)
            cycle.remove(crs)
            visited.add(crs)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return []
        return path