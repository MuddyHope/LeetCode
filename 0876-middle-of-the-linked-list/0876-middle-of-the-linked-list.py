# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        count = 0
        while temp != None:
            count+=1
            temp = temp.next
            
        
        mid = count//2
            
        i = 0
        temp = head
        print(head)
        print(head.next)
        while i != mid:
            i+=1
            temp = temp.next
        
        return temp
            
        