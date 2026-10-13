class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reach = 0
        for i in range(len(nums)-1):
            reach = max(reach, nums[i] + i)
            if reach >= len(nums) - 1:
                return True
            if reach <= i:
                return False

        return True
