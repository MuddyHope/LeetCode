"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        def pt(root):
            if root:
                for i in root.children:
                    s.append(i.val)
                    pt(i)
                    
        s = []
        if root:
            s.append(root.val)
        pt(root)
        return s