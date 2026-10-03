import collections
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        res = []
        for num in nums:
            seen[num] = seen.get(num, 0) + 1
        sorted_values = sorted(seen.items(), key = lambda x: x[1], reverse = True)
        res = [num for num, i in sorted_values[:k]]
        return res