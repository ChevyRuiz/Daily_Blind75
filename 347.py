import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = dict()
        for num in nums:
            if num in hashmap:
                hashmap[num] = hashmap[num] + 1
            else:
                hashmap[num] = 1

        max_heap = [(-count, num) for num, count in hashmap.items()]
        heapq.heapify(max_heap)

        ans = []
        for i in range(0, k):
            neg_largest_val, largest_key = heapq.heappop(max_heap)
            ans.append(largest_key)
        
        return ans
