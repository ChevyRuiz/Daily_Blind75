class Solution:
    def longestPalindrome(self, s: str) -> str:
        finalres = [0, 0, 0] # len, left, right
        for i in range(0, len(s)):
            res1 = self.palindromeLenFromMiddle(s, i, i) # odd case
            res2 = self.palindromeLenFromMiddle(s, i, i + 1) # even case
            if res1[0] > res2[0]:
                res = res1
            else:
                res = res2
            if res[0] > finalres[0]:
                finalres = res
        return s[finalres[1]:finalres[2] + 1]



    def palindromeLenFromMiddle(self, s, left, right):
        while(left >= 0 and right < len(s) and s[left] == s[right]):
            left -= 1
            right += 1
        # The loop goes updates the indices one step too long, so we need to correct it
        return [right - left - 1, left + 1, right - 1] # len, left, right
