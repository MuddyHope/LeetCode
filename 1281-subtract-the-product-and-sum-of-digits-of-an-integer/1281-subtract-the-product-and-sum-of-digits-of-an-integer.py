class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        #print(len(n))
        IntPro , IntSum = 1,0
        while n:
            IntPro *= n%10
            IntSum += n%10
            n = n//10
        return IntPro - IntSum