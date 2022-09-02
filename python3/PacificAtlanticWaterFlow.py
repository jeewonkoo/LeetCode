import collections
class Solution:
    def pacificAtlantic(self, heights):
        """
        type heights: List[List[int]]
        rtpye: List[List[int]]
        """
        m, n = len(heights), len(heights[0])
        pacific = [(0, i) for i in range(n)] + [(i, 0) for i in range(1, m)]
        atlantic = [(m-1, i) for i in range(n)] + [(i, n-1) for i in range(m-1)]
        
        def bfs(queue):
            visited = set()
            dq = collections.deque(queue)
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            while dq:
                x, y = dq.popleft()
                visited.add((x,y))
                for direction in directions:
                    new_x, new_y = direction[0]+x, direction[1]+y
                    if -1 < new_x < m and -1 < new_y < n and (new_x, new_y) not in visited and heights[new_x][new_y] >= heights[x][y]:
                        dq.append((new_x, new_y))
            return visited
        return bfs(pacific) & bfs(atlantic)