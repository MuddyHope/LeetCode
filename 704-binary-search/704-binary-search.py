class Solution:
    def search(self, nums: List[int], target: int) -> int:
        mid = 0 
        i = 0
        first = 0
        last = len(nums)
        while last > first:
            mid = (first+last)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                nums[:mid]
                last = mid
            else:
                nums[mid+1:]
                first = mid+1
        return -1