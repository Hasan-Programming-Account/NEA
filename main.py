piece = ['null','pawn','rook','bishop','knight','queen','king']

class board():
    def __init__(self):
        self.board = [[2,4,3,5,6,3,4,2],
                      [1,1,1,1,1,1,1,1],
                      [0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0],
                      [1,1,1,1,1,1,1,1],
                      [2,4,3,5,6,3,4,2]]
        
    def reset(self):
        self.board = [[2,4,3,5,6,3,4,2],
                      [1,1,1,1,1,1,1,1],
                      [0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0],
                      [1,1,1,1,1,1,1,1],
                      [2,4,3,5,6,3,4,2]]
        
    

a = board()
print(piece[a.board[0][5]])
