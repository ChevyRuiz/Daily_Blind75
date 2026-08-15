class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        currSum = 0

        for n in nums:
            currSum = max(0, currSum)
            currSum += n
            maxSub = max(maxSub, currSum)
        return maxSub
