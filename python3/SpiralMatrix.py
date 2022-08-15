class Solution:
    def spiralOrder(self, matrix):
        """
        type matrix: List[List[int]])
        return: List[List[int]]) -> List[int]
        """
        ans = []
        while matrix:
            ans += matrix.pop(0)
            matrix = list(zip(*matrix))[::-1]
        return ans
    
if __name__ == '__main__':
    s = Solution()
    print(s.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
    print(s.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))