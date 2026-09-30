class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        hashmap = defaultdict(list)
        #The plan is that we take each word and we do *at, b*t, ba*. 
        #We can do a bfs to find the minimum number of words within
        #the transformation sequence. 
        for word in wordList:
            for i in range(len(word)):
                key = word[:i] + "*" + word[i + 1:]
                hashmap[key].append(word)

        q = deque()
        visited = set()
        q.append((beginWord, 1))
        visited.add(beginWord)
        while q:
            word, level = q.popleft()
            if word == endWord:
                return level
            for i in range(len(word)):
                key = word[:i] + "*" + word[i + 1:]
                if key not in hashmap:
                    continue
                for neighbor in hashmap[key]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        q.append((neighbor, level + 1))
        return 0
        