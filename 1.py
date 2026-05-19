class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = []
        hashmap = dict()
        for i in range(0, len(nums)):
            hashmap[nums[i]] = i
        for i in range(0, len(nums)):
            if target - nums[i] in hashmap and i != hashmap[target - nums[i]]:
                indices.append(i)
                indices.append(hashmap[target - nums[i]])
                break
        return indices
