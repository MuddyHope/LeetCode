class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        #base case
        if len(s) > len(t):
            return False
        if len(s) == 0:
            return True
        
        #pointers
        i,j = 0,0
        
        while j < len(t):
            if s[i] == t[j]:
                i+=1
                j+=1
                if len(s) == i:
                    return True
            else:
                j+=1
        return False