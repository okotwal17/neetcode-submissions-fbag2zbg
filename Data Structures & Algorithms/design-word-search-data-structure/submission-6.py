class Node:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = Node()
            cur = cur.children[c]
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        def dfs(node, j):
            cur = node
            for i in range(j, len(word)):
                if word[i] == ".":
                    for c in cur.children:
                        if dfs(cur.children[c], i + 1):
                            return True
                    return False
                else:
                    if word[i] not in cur.children:
                        return False
                    cur = cur.children[word[i]]
            return cur.endOfWord
        return dfs(self.root, 0)

