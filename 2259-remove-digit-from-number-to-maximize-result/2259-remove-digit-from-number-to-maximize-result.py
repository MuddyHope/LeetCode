class Solution(object):
    def removeDigit(self, number, digit):
        """
        :type number: str
        :type digit: str
        :rtype: str
        """
        i = 0
        new_res = 0
        while i < len(number):
            if number[i] == digit:
                new_res = max(number[:i]+number[i+1:], new_res)
            i+=1
        return new_res