class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        mylist = [0,1,1,2]
        first,second = 1,2
        for i in range(4,30):
            #sums = first + second
            mylist.append(mylist[i-1] + mylist[i-2])
        print(mylist)
        
        if n == 1:
            return 1
        elif n == 0:
            return 0
        else:
            return mylist[n-1] + mylist[n-2]