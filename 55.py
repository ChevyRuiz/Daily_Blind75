class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        O(n^n)
        def dfs(currIndex, targetIndex, nums):
            # Base case
            if currIndex >= targetIndex:
                return True
            # Recursive case
            positions = [i + 1 for i in range(nums[currIndex])]
            boolpositions = []
            for position in positions:
                boolpositions.append(dfs(currIndex + position, targetIndex, nums))
            
            return any(boolpositions)

        targetIndex = len(nums) - 1
        currIndex = 0
        return dfs(currIndex, targetIndex, nums)
        """

        """
        O(n^2)
        dp = [False] * len(nums)
        for i in range(len(nums) -1, -1, -1):
            # Base case
            if i + 1 >= len(nums):
                dp[i] = True
            else:
                positions = [j + 1 for j in range(nums[i])]
                boolpositions = []
                for position in positions:
                    if i + position < len(nums):
                        boolpositions.append(dp[i + position])
                dp[i] = any(boolpositions)
        return dp[0]
        """

        goal = len(nums) - 1
        for i in range(len(nums) -1, -1, -1):
            if i + nums[i] >= goal:
                goal = i

        return True if goal == 0 else False
