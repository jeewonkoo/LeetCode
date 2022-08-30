import collections

class Solution:
    def numIslands(self, grid):
        """
        type grid: List[List[str]]
        rtype: int
        """
        
        def isValid(x, y):
            return (x > -1 and y > -1) and (x < len(grid) and y < len(grid[0]))
        
        def bfs(grid, i, j):
            #use deque since it is efficient than list
            queue = collections.deque()
            queue.append((i,j))
            #After you append to queue, change it to 0
            grid[i][j] = "0"     
            # print(queue)
            while queue:
                x, y = queue.popleft()
                directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
                #iterate adjacent coordinates to find if it is land or water 
                for direction in directions:
                    new_x, new_y = x + direction[0], y + direction[1]
                    if isValid(new_x, new_y) and grid[new_x][new_y] == "1":
                        queue.append((new_x, new_y))
                        grid[new_x][new_y] = "0"
                    
        #number of islands
        count = 0
        
        #iterate islands 
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                #if grid[i][j] is equal to 1, do bfs
                if grid[i][j] == "1": 
                    bfs(grid, i, j)
                    count +=1 
                
        
        return count 

if __name__ == '__main__': 
    s = Solution()
    print(s.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]))
    print(s.numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]))