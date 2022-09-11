class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
    
        leftsum = 0

        rightsum = sum(nums)

        for i in range(len(nums)):
            rightsum-=nums[i]

            if leftsum == rightsum:
                return i
            leftsum+=nums[i]
        return -1
        
#         i,j = 0,len(nums)-1
        
#         for k in range(1,len(nums)):
#             temp_sum += nums[k]
#             if(temp_sum == 0):
#                 return 0
            
#         while i < j:
#             left_sum += nums[i]
#             if(left_sum == right_sum):
#                 return i+1
#             right_sum += nums[j]
#             i+=1
#             j-=1
#         return -1

        