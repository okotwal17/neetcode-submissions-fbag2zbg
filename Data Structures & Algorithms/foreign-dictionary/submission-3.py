class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adjList = {c : set() for w in words for c in w}
        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i+1]
            shorter = min(len(words[i]), len(words[i+1]))
            if len(word1) > len(word2) and word1[:shorter] == word2[:shorter]:
                return ""
            for j in range(shorter):
                if word1[j] != word2[j]:
                    adjList[word1[j]].add(word2[j])
                    break

        res = []
        visited = set()
        seen = set()
        def dfs(curNode):
            if curNode in seen:
                return False
            if curNode in visited:
                return True
            seen.add(curNode)
            for elem in adjList[curNode]:
                if not dfs(elem):
                    return False
            seen.remove(curNode)
            visited.add(curNode)
            res.append(curNode)
            adjList[curNode] = set()
            return True
        for c in adjList:
            if not dfs(c):
                return ""
        res.reverse()
        return "".join(res)
