class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        for l in s:
            t = t.replace(l,"",1)
        return len(t) == 0
