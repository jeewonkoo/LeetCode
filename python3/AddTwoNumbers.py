# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        type l1: Optional[ListNode], l2: Optional[ListNode]
        rtype Optional[ListNode]
        """
        head = curr = ListNode()
        overflow = 0
        
        while l1 or l2:
            value = 0
            if l1: 
                value += l1.val
                l1 = l1.next
            if l2: 
                value += l2.val
                l2 = l2.next
            value += overflow 
            overflow = 0
            if value >= 10:
                overflow += 1
                value %= 10
            curr.next = ListNode(value)
            curr = curr.next
            
        if overflow: 
            curr.next = ListNode(1)
            curr = curr.next
        return head.next