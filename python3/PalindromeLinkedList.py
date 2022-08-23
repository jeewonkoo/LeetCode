# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome_stack(self, head) -> bool:
        """
        type head:: Optional[ListNode]
        rtype: bool
        """
        stack = []
        curr = head
        
        #add to values to stack
        while curr:
            stack.append(curr.val)
            curr = curr.next
        
        #iterate linked list again to compare if value matches with popped elem from stack
        while head:
            target = stack.pop()
            #if value of head and element from stack doesn't match it's not palindrome so return False
            if head.val != target: return False
            head = head.next
        #if it iterates till the end, then all values of list and stack match, so return True
        return True

    def isPalindrome_pythonic_way(self, head) -> bool:
        """
        type head:: Optional[ListNode]
        rtype: bool
        """
        stack = []
        curr = head
        while curr:
            stack.append(curr.val)
            curr = curr.next
        return stack == stack[::-1]