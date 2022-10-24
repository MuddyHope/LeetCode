"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        temp = root
        res = []
        def helperfunc(Node):
            if Node:
                for i in Node.children:
                    res.append(i.val)
                    helperfunc(i)
        if temp == None:
            return res
        else:
            res.append(temp.val)
        for i in temp.children:
            res.append(i.val)
            helperfunc(i)
            
        
        return res