class Solution:
    def setZeroes(self, matrix):
        
        """
        :type matrix: List[List[int]]
        Do not return anything, modify matrix in-place instead.
        """
        coordinates = []
        row = len(matrix)
        col = len(matrix[0])
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0 : coordinates.append((i,j))

        for coordinate in coordinates: 
            for i in range(row):
                if matrix[i][coordinate[1]] != 0: matrix[i][coordinate[1]] = 0
            for j in range(col):
                if matrix[coordinate[0]][j] != 0: matrix[coordinate[0]][j] = 0
        return matrix
                
if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.setZeroes([[1,1,1],[1,0,1],[1,1,1]]))