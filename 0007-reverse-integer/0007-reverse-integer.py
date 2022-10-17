class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            return -1 * self.reverseUtil(-x)
        return self.reverseUtil(x)
    
    def reverseUtil(self, x):
        result = 0
        while x != 0:
            digit = x%10
            result = result * 10 + digit
            x = int(x/10)
        if result > (2**31) - 1 or result < (-2**31):
            return 0
        else:
            return result