class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum = 0
        temp = []
        for i in range(len(nums)):
            sum = sum + nums[i]
            temp.insert(i,sum)
        return temp