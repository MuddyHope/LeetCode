class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        length = len(nums)
        for i in range(0, length-1, 2):
            res += nums[i]
        return res