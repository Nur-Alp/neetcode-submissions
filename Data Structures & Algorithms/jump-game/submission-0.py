class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        for r in range(n - 1):
            if nums[r] == 0:
                if not any(l + nums[l] > r for l in range(r)):
                    return False
        return True