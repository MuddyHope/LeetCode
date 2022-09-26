class Solution:
    def longestPalindrome(self, s: str) -> int:
        flag = False
        count = 0 
        odd_num = 0
        q = []
        for j in set(s):
            q.append(j)
        for i in range(len(q)):
            if  s.count(q[i])  % 2 != 0:
                flag = True
                odd_num += s.count(q[i])
                odd_num -= 1
            elif s.count(q[i]) % 2 == 0:
                count += s.count(q[i])
        if flag == True:
            return count + odd_num + 1
        else:
            return count + odd_num
            
            