class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courseList = {i : [] for i in range(numCourses)}
        for c1, c2 in prerequisites:
            courseList[c1].append(c2)
        visited = set()

        output = []
        visit, cycle = set(), set()
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True
            
            cycle.add(crs)
            for pre in courseList[crs]:
                if not dfs(pre):
                    return False
            cycle.remove(crs)
            visit.add(crs)
            output.append(crs)
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return []
        return output