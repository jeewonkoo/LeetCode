from collections import defaultdict

class Solution:
    def diagonalSort(self, mat):
        """
        type mat: List[List[int]]
        rtype: List[List[int]]
        """
        n, m = len(mat), len(mat[0])
        d = defaultdict(list)
        
        #phase 1: store
        for i in range(n):
            for j in range(m):
                d[i-j].append(mat[i][j])
        
        #phase 2: sort
        for i in d:
            d[i].sort()
        
        #phase 3: put it back 
        for i in range(n):
            for j in range(m):
                # print(d[i-j])
                mat[i][j] = d[i-j][0]
                d[i-j] = d[i-j][1:]
        
        return mat

if __name__ == '__main__':
    s = Solution()
    print(s.diagonalSort([[3,3,1,1],[2,2,1,2],[1,1,1,2]]))
    print(s.diagonalSort([[11,25,66,1,69,7],[23,55,17,45,15,52],[75,31,36,44,58,8],[22,27,33,25,68,4],[84,28,14,11,5,50]]))