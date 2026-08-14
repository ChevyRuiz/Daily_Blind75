class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftToRight = []
        rightToLeft = []
        for i in range(len(nums)):
            if i > 0:
                leftToRight.append(nums[i] * leftToRight[i - 1])
            else:
                leftToRight.append(nums[i])
        for i in range(len(nums) - 1, -1, -1):
            if i < len(nums) - 1:
                rightToLeft.insert(0, nums[i] * rightToLeft[0])
            else:
                rightToLeft.append(nums[i])

        ans = []
        for i in range(len(nums)):
            left = 1
            right = 1
            if i > 0:
                left = leftToRight[i - 1]
            if i < len(nums) - 1:
                right = rightToLeft[i + 1]
            ans.append(left * right)

        return ans
