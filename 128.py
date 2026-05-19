class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset  = set(nums)
        longest = 0
        for item in hashset:
            if item - 1 not in hashset:
                length = 1
                while item + length in hashset:
                    length += 1
                if length > longest:
                    longest = length
        return longest
            
# Solution 4: https://neetcode.io/solutions/longest-consecutive-sequence