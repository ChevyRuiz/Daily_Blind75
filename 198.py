class Solution:
    """
    def rob(self, nums: List[int]) -> int:
        def dfs(house, nums):
            # Base case: 
            if house >= len(nums):
                return 0
            
            # Recursive case
            localMax = 0
            for adj in range(house + 2, len(nums)):
                localMax = max(localMax, dfs(adj, nums))
            return nums[house] + localMax

        ans = 0
        localMax = 0
        for house in range(len(nums)):
            localMax = dfs(house, nums)
            if localMax > ans:
                ans = localMax

        return ans
    """
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2
