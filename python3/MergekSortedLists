# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists):
        """
        type    lists List[Optional[ListNode]]
        rtype   Optional[ListNode]
        """
        heap = []
        for list_ in lists: 
            while list_:
                heapq.heappush(heap, list_.val)
                list_ = list_.next
        
        head = curr = ListNode()
        
        while heap:
            node_value = heapq.heappop(heap)
            temp = ListNode(node_value)
            curr.next = temp
            curr = temp
            
        return head.next