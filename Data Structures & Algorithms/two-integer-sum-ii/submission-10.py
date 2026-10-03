class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}
        for i, n in enumerate(numbers):
            goal = target - n
            if goal in seen:
                return [seen[goal] + 1, i + 1]
            else: 
                seen[n] = i 
        
