import collections
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root):
        """
        type root: Optional[TreeNode]
        rtype: List[float]"""
        avg_level = []
        queue = collections.deque()
        queue.append(root)
        queue.append(None)
        total, num_of_node = 0, 0
        while queue:
            curr = queue.popleft()
            if not curr: 
                avg_level.append(total / num_of_node)
                total = num_of_node = 0
                if queue: queue.append(None)
            else: 
                total += (curr.val)
                num_of_node += 1
                if curr.left: queue.append(curr.left)
                if curr.right: queue.append(curr.right)
        return avg_level