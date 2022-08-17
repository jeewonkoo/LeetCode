#  Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

import collections

class Solution:
    #BFS version
    def cloneGraph_BFS(self, node):  
        """
        type node: Node 
        return Node
        """
        #input validation
        if not node: return node
        
        #create queue and dictionary to count cloned node
        queue, cloned = collections.deque([node]), {}
        
        #clone node and add it to cloned
        node_copy = Node(node.val, [])
        cloned[node] = node_copy 
        
        #while queue
        while queue:
            #deque first element
            curr = queue.popleft()
            #iterate neighbor
            for neighbor in curr.neighbors:
                #if neighbor is not cloned 
                if neighbor not in cloned: 
                    #clone neighbor and add it to cloned 
                    neighbor_copy = Node(neighbor.val, [])
                    cloned[neighbor] = neighbor_copy
                    #add it to queue so we can go iterate again 
                    queue.append(neighbor)
                
                #if neighbor is cloned, 
                #add cloned[neighbor] to cloned[curr].neighbors 
                cloned[curr].neighbors.append(cloned[neighbor])
                
        return cloned[node]
            