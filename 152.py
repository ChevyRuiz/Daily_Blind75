import heapq
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        O(n^2)
        maxProduct = nums[0]
        currProduct = 1
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                currProduct = currProduct * nums[j]
                maxProduct = max(maxProduct, currProduct)
            currProduct = 1
        return maxProduct
        """
        res = max(nums)
        currMin, currMax = 1, 1
        for n in nums:
            tmp = currMax * n
            currMax = max(n * currMax, n * currMin, n)
            currMin = min(tmp, n * currMin, n)
            res = max(res, currMax)
        return res
