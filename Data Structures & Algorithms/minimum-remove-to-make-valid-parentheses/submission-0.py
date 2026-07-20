class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        "Do some bs up here"
        stack = []
        for i in range(len(s)):
            if s[i] not in "()":
                continue
            if s[i] == ")" and stack and s[stack[-1]] == "(":
                stack.pop()
            else:
                stack.append(i)

        "Go thrgough down here"
        idxs = set(stack)
        res = ""
        for i in range(len(s)):
            if i not in idxs:
                res += s[i]
        return res