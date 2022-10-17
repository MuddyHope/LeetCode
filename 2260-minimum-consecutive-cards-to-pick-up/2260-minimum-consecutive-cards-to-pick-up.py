class Solution(object):
    def minimumCardPickup(self, cards):
        """
        :type cards: List[int]
        :rtype: int
        """
        mydict = {}
        
        #input - [3,4,2,3,4,7]
        #         0,1,2,3,4,5
        
        res = 10000000
        j = 0
        doubles = False
        for i in cards:
            if i in mydict:
                res = min(res, j - mydict[i])
                mydict[i] = j
                doubles = True
            else:
                mydict[i] = j
            j+=1
        
        if doubles == True:
            return res+1
        else:
            return -1
        