class Node:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = Node()
            cur = cur.children[c]
        cur.endOfWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Node()
        for word in words:
            trie.addWord(word)
        ROWS, COLS = len(board), len(board[0])
        visited = set()
        directions = [[1,0], [0, 1], [-1, 0], [0, -1]]
        res = set()
        def dfs(r, c, path, node):
            if (r < 0 or c < 0 or 
            r == ROWS or c == COLS
            or (r, c) in visited
            or board[r][c] not in node.children):
                return
            visited.add((r,c))
            node = node.children[board[r][c]]
            if node.endOfWord:
                res.add(path + board[r][c])
            for dr, dc in directions:
                dfs(r + dr, c + dc, path + board[r][c], node)
            visited.remove((r,c))
        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, "", trie)
        return list(res)
            
            
