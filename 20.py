class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {
            "}" : "{",
            ")" : "(",
            "]" : "["
        }
        stack = []
        for char in s:
            stack.append(char)
            while len(stack) > 1 and stack[-1] in hashmap:
                if stack[-2] == hashmap[stack[-1]]:
                    stack.pop()
                    stack.pop()
                else:
                    break
        return stack == []
