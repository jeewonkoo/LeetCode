class Solution:
    def isValidSudoku(self, board):
        """
        type board: List[List[str]]
        rtype: bool 
        """
        def isValid(line):
            """
            type line: : List[str]
            rtype: bool 
            """
            seen = {}
            for i in line: 
                if i in seen: return False 
                if i != ".": seen[i] = seen.get(i, 0) + 1
            return True
        
        def isValidSquare(square, x: int, y: int):
            """
            type square: List[List[str]], x: int, y: int
            rtype: bool 
            """
            seen = {}
            for i in range(x, x+3):
                for j in range(y, y+3):
                    if square[i][j] in seen: return False
                    if square[i][j] != ".": seen[square[i][j]] = seen.get(square[i][j], 0) + 1
            return True
        
        #check if row and col is valid
        for i in range(9):
						#row
            if not isValid(board[i]): return False
						#col
            if not isValid(list(zip(*board))[i]): return False
        #Or check if col is valid alone
        #for i in zip(*board):
        #    if not isValid(i): return False
            
        #check if square is valid
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                if not isValidSquare(board, i, j): return False
        
        return True

if __name__ == '__main__': 
    s = Solution()
    print(s.isValidSudoku([["5","3",".",".","7",".",".",".","."],
                            ["6",".",".","1","9","5",".",".","."],
                            [".","9","8",".",".",".",".","6","."],
                            ["8",".",".",".","6",".",".",".","3"],
                            ["4",".",".","8",".","3",".",".","1"],
                            ["7",".",".",".","2",".",".",".","6"],
                            [".","6",".",".",".",".","2","8","."],
                            [".",".",".","4","1","9",".",".","5"],
                            [".",".",".",".","8",".",".","7","9"]])) #prints True
    print(s.isValidSudoku([["7","3",".",".","7",".",".",".","."],
                            ["6",".",".","1","9","5",".",".","."],
                            [".","9","8",".",".",".",".","6","."],
                            ["8",".",".",".","6",".",".",".","3"],
                            ["4",".",".","8",".","3",".",".","1"],
                            ["7",".",".",".","2",".",".",".","6"],
                            [".","6",".",".",".",".","2","8","."],
                            [".",".",".","4","1","9",".",".","5"],
                            [".",".",".",".","8",".",".","7","9"]])) #prints False - invalid row
    print(s.isValidSudoku([["6","3",".",".","7",".",".",".","."],
                            ["6",".",".","1","9","5",".",".","."],
                            [".","9","8",".",".",".",".","6","."],
                            ["8",".",".",".","6",".",".",".","3"],
                            ["4",".",".","8",".","3",".",".","1"],
                            ["7",".",".",".","2",".",".",".","6"],
                            [".","6",".",".",".",".","2","8","."],
                            [".",".",".","4","1","9",".",".","5"],
                            [".",".",".",".","8",".",".","7","9"]])) #prints False - invalid col
    print(s.isValidSudoku([["9","3",".",".","7",".",".",".","."],
                            ["6",".",".","1","9","5",".",".","."],
                            [".","9","8",".",".",".",".","6","."],
                            ["8",".",".",".","6",".",".",".","3"],
                            ["4",".",".","8",".","3",".",".","1"],
                            ["7",".",".",".","2",".",".",".","6"],
                            [".","6",".",".",".",".","2","8","."],
                            [".",".",".","4","1","9",".",".","5"],
                            [".",".",".",".","8",".",".","7","9"]])) #prints False - invalid square