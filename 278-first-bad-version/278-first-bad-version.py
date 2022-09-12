# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        start = 0
        end = n
        mid = 0
        while start < end:
            mid = (start+end)//2
            if isBadVersion(mid):
                end = mid
            else:
                start = mid+1
        if isBadVersion(mid):
            return mid
        else: return mid+1
        