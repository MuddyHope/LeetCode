class Solution:
    def arraySign(self, nums: List[int]) -> int:
        neg = 0
        for i in nums:
            if i == 0:
                return 0
            if i < 0:    #negative numbers
                neg +=1
                
        if neg%2 == 0:
            return 1
        else:
            return -1
        