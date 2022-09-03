import collections

#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def invertTree_recursive(self, root):
        if not root: return
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root
    
    def invertTree_BFS(self, root):
        queue = collections.deque()
        queue.append(root)
        
        while queue:
            curr = queue.popleft()
            if curr:
                curr.left, curr.right = curr.right, curr.left
                queue.append(curr.left)
                queue.append(curr.right)
        
        return root
    
    def invertTree_DFS(self, root):
        stack = [root]
        
        while stack:
            curr = stack.pop()
            if curr: 
                curr.left, curr.right = curr.right, curr.left
                stack.extend([curr.left, curr.right])
        
        return root