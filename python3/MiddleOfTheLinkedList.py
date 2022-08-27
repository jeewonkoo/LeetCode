# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head):
        """
        type head: Optional[ListNode
        rtype: Optional[ListNode]
        """
        slow = fast = head 
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            print(fast.val, slow.val)
        return slow 