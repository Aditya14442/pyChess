class piece:
    def __init__(self,colour,value,type):
        self.colour=colour
        self.type=type
        self.value=value
        if colour=='BLACK':
            self.type=chr(ord(self.type[0])+32)
    def __str__(self):
        return self.type
class empty(piece):
    def __init__(self):
        self.colour='NULL'
        self.type='x'
        self.value=0
class king(piece):
    def __init__(self,colour):
        super().__init__(colour,40,'K')
class queen(piece):
    def __init__(self,colour):
        super().__init__(colour,9,'Q')
class knight(piece):
    def __init__(self,colour):
        super().__init__(colour,3,'N')
class bishop(piece):
    def __init__(self,colour):
        super().__init__(colour,3,'B')
class rook(piece):
    def __init__(self,colour):
        super().__init__(colour,5,'R')
class pawn(piece):
    def __init__(self,colour):
        super().__init__(colour,1,'P')
class square:
    def __init__(self,colour):
        self.colour=colour
        self.housing=None
    def __str__(self):
        return self.housing.type
class chessBoard:
    def __init__(self):
        self.board=[]
        for i in range(8):
            self.board.append([None,None,None,None,None,None,None,None])
            for j in range(8):
                if (i+j)%2==0:
                    self.board[i][j]=(square('BLACK'))
                else:
                    self.board[i][j]=(square('WHITE'))
    def __getitem__(self, item):
        return self.board[item]
    def __setitem__(self, key, value):
        self.board[key]=value
def printBoard(gameBoard):
    for i in range(8):
        for j in range(8):
            print(gameBoard[7-i][j],end=' ')
        print()
class game:
    def __init__(self):
        gameBoard=chessBoard()
        piecesAlive=['WK','BK','WQ','BQ']
        deadPieces=[]
        for i in range(2):
            piecesAlive.append('WR')
            piecesAlive.append('BR')
            piecesAlive.append('WB')
            piecesAlive.append('BB')
            piecesAlive.append('WN')
            piecesAlive.append('BN')
        for i in range(8):
            piecesAlive.append('WP')
            piecesAlive.append('BP')
        for i in range(8):
            gameBoard[1][i].housing=pawn('WHITE')
        for i in range(8):
            gameBoard[6][i].housing=pawn('BLACK')
        gameBoard[0][0].housing,gameBoard[0][7].housing,gameBoard[7][0].housing,gameBoard[7][7].housing=rook('WHITE'),rook('WHITE'),rook('BLACK'),rook('BLACK')
        gameBoard[0][1].housing, gameBoard[0][6].housing, gameBoard[7][1].housing,gameBoard[
            7][6].housing=knight('WHITE'),knight('WHITE'),knight('BLACK'),knight('BLACK')
        gameBoard[0][2].housing, gameBoard[0][5].housing, gameBoard[7][2].housing, gameBoard[
            7][5].housing = bishop('WHITE'), bishop('WHITE'), bishop('BLACK'), bishop('BLACK')
        gameBoard[0][3].housing, gameBoard[0][4].housing, gameBoard[7][3].housing, gameBoard[
            7][4].housing =queen('WHITE'),king('WHITE'),queen('BLACK'),king('BLACK')
        for i in range(8):
            for j in range(8):
                if gameBoard[i][j].housing==None:
                    gameBoard[i][j].housing=empty()
        printBoard(gameBoard)
    def move(self,turn):
        toMove=input("Enter piece to move: ")
        # while(ord(toMove[0])<97 or ord(toMove[0])>104 or )

mygame=game()
