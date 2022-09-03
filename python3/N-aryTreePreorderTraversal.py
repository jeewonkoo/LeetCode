"""
# Definition for a Node.
"""
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder_recursive(self, root):
        def dfs(root, output): 
            if not root: 
                return 
            output.append(root.val)
            for child in root.children:
                dfs(child, output)
                
        output = []
        dfs(root, output)
        return output

    def preorder_iterative(self, root):
        if not root: return None
        stack = [root]
        output = []
        while stack:
            curr = stack.pop()
            output.append(curr.val)
            stack.extend(curr.children[::-1])
        return output