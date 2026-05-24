class Solution:

    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(0, len(s)):
            count += self.countPalsFromMiddle(s, i, i) # odd case
            count += self.countPalsFromMiddle(s, i, i + 1) # even case
        return count

    def countPalsFromMiddle(self, s, left, right):
        count = 0
        leftIndex = left
        rightIndex = right
        while leftIndex >= 0 and rightIndex < len(s):
            if s[leftIndex] == s[rightIndex]:
                count += 1
                leftIndex -= 1
                rightIndex += 1
            else:
                break
        return count
