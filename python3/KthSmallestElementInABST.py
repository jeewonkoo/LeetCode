import collections
# Definition for a binary tree node.
class TreeNode:
    def Node(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def kthSmallest_naive(self, root, k: int):
        queue = collections.deque()
        queue.append(root)
        elements = []
        while queue:
            curr = queue.popleft()
            if curr: 
                elements.append(curr.val)
                if curr.left: queue.append(curr.left)
                if curr.right: queue.append(curr.right)
        
        elements = sorted(elements)
        return elements[k-1]
    
    def kthSmallest_optimize(self, root, k: int):
        stack = []
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left 
            
            node = stack.pop()
            k -= 1
            if k == 0: 
                print(stack)
                return node.val
            curr = node.right