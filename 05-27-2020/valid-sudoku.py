# https://leetcode.com/problems/valid-sudoku/

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        n = len(board)
        for i in range(n):
            for j in range(n):
                if(board[i][j] == '.'):
                    board[i][j] = 0
                else:
                    board[i][j] = int(board[i][j])
        
        
        # checking for horizontal and vertical
        for i in range(n):
            record1 = [0]*10
            record2 = [0]*10
            for j in range(n):
                if(record1[board[i][j]] == 0):
                    record1[board[i][j]] = 1
                elif(board[i][j] == 0):
                    record1[board[i][j]] += 1
                else:
                    # print(1, i,j)
                    return False
                
                if(record2[board[j][i]] == 0):
                    record2[board[j][i]] = 1
                elif(board[j][i] == 0):
                    record2[board[j][i]] += 1
                else:
                    # print(2, i,j,board[i][j])
                    return False
                
        
        
        
        l = int(sqrt(n))
        # checking for sub-box
        for i in range(0,n,l):
            for j in range(0,n,l):
                record = [0]*10
                for x in range(i, i+l):
                    for y in range(j,j+l):
                        if(record[board[x][y]] == 0):
                            record[board[x][y]] = 1
                        elif(board[x][y] == 0):
                            record[board[x][y]] += 1
                        else:
                            # print(3, i,j)
                            return False
                        
        return True
        
                
                    
