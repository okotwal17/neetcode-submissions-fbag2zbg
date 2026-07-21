class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjacencyList = defaultdict(list)
        for c1, c2 in prerequisites:
            adjacencyList[c2].append(c1)
        visited = set()
        def dfs(node):
            if node in visited:
                return False
            visited.add(node)
            for preReq in adjacencyList[node]:
                if not dfs(preReq):
                    return False
            visited.remove(node)
            adjacencyList[node] = []
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True