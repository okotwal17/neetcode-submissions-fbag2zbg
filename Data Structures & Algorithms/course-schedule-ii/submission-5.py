class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjacencyList = defaultdict(list)
        for p1, p2 in prerequisites:
            adjacencyList[p1].append(p2)
        visited = set()
        seen = set()
        res = []
        def dfs(node):
            if node in seen:
                return False
            if node in visited:
                return True
            seen.add(node)
            for n in adjacencyList[node]:
                if not dfs(n):
                    return False
            seen.remove(node)
            res.append(node)
            visited.add(node)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return []
        return res

            