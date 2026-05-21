class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longestLen = 0
        currentLen = 0
        beginWindow = -1
        hashmap = dict()
        for i in range(0, len(s)):
            endWindow = i
            # The second condition is tricky, it's there to make sure beginWindow only goes forward
            if s[i] in hashmap and hashmap[s[i]] > beginWindow:
                beginWindow = hashmap[s[i]]
            hashmap[s[i]] = i
            currentLen = endWindow - beginWindow
            if currentLen > longestLen:
                longestLen = currentLen   

        return longestLen

# I used the sliding window technique
