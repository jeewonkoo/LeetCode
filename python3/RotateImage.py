class Solution:
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        """
        type matrix: List[List[int]]
        rtype: None
        """
        
        def transpose(matrix):
            for i in range(len(matrix)):
                for j in range(i+1, len(matrix[0])):
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        def reverse(matrix):
            for i in range(len(matrix)): 
                for j in range(len(matrix)//2):
                    matrix[i][j], matrix[i][-1-j] = matrix[i][-1-j], matrix[i][j]
        transpose(matrix)
        reverse(matrix)

if __name__ == '__main__':
    s = Solution()
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    s.rotate(matrix)
    print(matrix)

    matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    s.rotate(matrix)
    print(matrix)
