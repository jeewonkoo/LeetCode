import collections

class Solution:
    def solve(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        """
        type board: List[List[str]]
        rtype: None
        """
        
        def is_valid(i, j):
            return (-1 < i < len(board) and -1 < j < len(board[0]))
        
#         def bfs(board, i, j):
            
#             queue.append((i,j))
            
#             while queue:
#                 x, y = queue.popleft()
#                 board[x][y] = "N"
#                 # directions = [(0,1), (1,0), (0, -1), (-1, 0)]
#                 for direction in [(0,1), (1,0), (0, -1), (-1, 0)]:
#                     new_x, new_y = x + direction[0], y + direction[1]
#                     if is_valid(new_x, new_y) and board[new_x][new_y] == "O":
#                         queue.append((new_x,new_y))

        queue = collections.deque()        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (i==0 or j==0 or i==len(board)-1 or j==len(board[0])-1) and board[i][j] =="O":
                    # print(i,j)
                    queue.append((i,j))
                    
        while queue:
            x, y = queue.popleft()
            board[x][y] = "N"
            directions = [(0,1), (1,0), (0, -1), (-1, 0)]
            for direction in directions:
                new_x, new_y = x + direction[0], y + direction[1]
                if is_valid(new_x, new_y) and board[new_x][new_y] == "O":
                    queue.append((new_x,new_y))
        
        
        # print(board)
        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] = "O" if board[i][j] == "N" else "X"
   