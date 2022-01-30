import time
import emoji
import random
from matplotlib import pyplot as plt

class tictactoe:
    def __init__(self):
        self.board = [
        [" "," "," "],
        [" "," "," "],
        [" "," "," "]
        ]
        ''' setting intial color for matrix'''
        self.steroidboard=[[(155, 149, 163)]*3 for _ in range(3)]
        self.uv=" "
        self.cv=" "

    def inputhuman(self):
        #inputting co-ordinates from the user
        print("Enter Co-ordinates :")
        i=int(input("Enter i : "))
        j=int(input("enter j : "))
        if self.board[i][j] == " " and i<3 and j<3:
            self.board[i][j]=self.uv

        else :
            print("Invalid move")
            print("Enter again ")
            self.inputhuman()
    def display(self):

        ''' updating display matrix based x and o to respective colors'''
        for i in range(3):
            for j in range(3):
                if self.board[i][j]!=" ":
                    if self.board[i][j]=="x" or self.board[i][j]=="X":
                        self.steroidboard[i][j]=(163, 108, 93)
                    else:
                        self.steroidboard[i][j] = (118, 90, 158)
        plt.imshow(self.steroidboard, interpolation='nearest')
        plt.show()


        for rows in self.board:
            print(rows)
    def minimax(self,board,depth,ismaximizing):
        result = self.checkwinner()
        if result =="x" :
            score= -1

            return score
        elif result =="o" :
            score= +1

            return score
        elif result == "draw":
            score= 0

            return score

        if ismaximizing :
            bestscore = 2
            for i in range(3):
                for j in range(3):
                    if board[i][j] == " ":
                        board[i][j]="x"
                        score = self.minimax(board, depth+1, False)
                        board[i][j] = " "
                        bestscore = min(bestscore, score)
            return bestscore
        else:
            bestscore = -2
            for i in range(3):
                for j in range(3):
                    if board[i][j] == " ":
                        board[i][j]="o"
                        score = self.minimax(board, depth+1, True)
                        board[i][j] = " "
                        bestscore = max(bestscore, score)
            return bestscore



    def computerplay(self):

        bestscore = -100
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == " " :
                    self.board[i][j]= self.cv
                    score = self.minimax(self.board,0,True)
                    self.board[i][j]=" "
                    if(score > bestscore):
                        bestscore=score
                        bestmove = [i,j]
        print(str(bestmove[0])+","+ str(bestmove[1])+" is the best move based on all possiblities using minmax algorithm ")
        self.board[bestmove[0]][bestmove[1]]=str(self.cv)



    def checkwinner(self):
    #rows check

        for rows in range(3):

            if self.board[rows][0] == self.board[rows][1] and self.board[rows][0] == self.board[rows][2] and self.board[rows][0] != " " :
                    return self.board[rows][0]
    #cols check
        for cols in range(3):

            if self.board[0][cols] == self.board[1][cols] and self.board[0][cols] == self.board[2][cols] and self.board[0][cols] != " ":
                return self.board[0][cols]
    #dialognal check
        if self.board[0][0]==self.board[1][1] and self.board[0][0]==self.board[2][2] and self.board[0][0] != " " :
            return self.board[0][0]
        if self.board[0][2]==self.board[1][1] and self.board[0][2]==self.board[2][0] and self.board[0][2] != " " :
            return  self.board[1][1]
        else :
            c=0
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] != " ":
                        c=c+1
            if c == 9 :
                return  "draw"
            return ""


    def play(self):

        n=0
        print("-----Welcome to TicTacToe------")
        print("Tossing a Coin ..... ")
        for i in range(3):
            time.sleep(1)
        c=random.choice([0, 1])
        if c==0:
            print("Computer won the toss")
            self.cv=random.choice(["X", "O"])
            if self.cv=="X":
                self.uv="O"
            else:
                self.uv="X"
            print("Computer has Chosen its Character as:",self.cv)
        else:
            print(" You have won the toss")
            print("Enter Your Character")
            self.uv=str(input())


        while n < 10:

            if c==0:
                self.display()
                result = self.checkwinner()
                if result != "" and result != "draw":
                    print(self.checkwinner() + " is winneer")
                elif result == "draw":
                    print("Draw")

                print("......Computer Playing......")
                for i in range(3):
                    time.sleep(1)
                self.computerplay()
                n=n+1
                self.display()
                result = self.checkwinner()


                if result != "" and result != "draw":
                    print(result + " is winneer")
                    break
                elif result == "draw":
                    print("--------Draw  : "+emoji.emojize(":zipper-mouth_face:")+"--------")
                    break
                self.inputhuman()
                n=n+1

            else:
                self.display()
                result = self.checkwinner()
                if result != "" and result != "draw":
                    print(self.checkwinner() + " is winneer")
                    break
                elif result == "draw":
                    print("Draw")
                    break
                self.inputhuman()
                n = n + 1
                self.display()
                if result != "" and result != "draw":
                    print(result + " is winneer")
                    break
                elif result == "draw":
                    print("--------Draw  : " + emoji.emojize(":zipper-mouth_face:") + "--------")
                    break
                print("......Computer Playing......")
                for i in range(3):
                    time.sleep(1)
                self.computerplay()
                n = n + 1

'''
define a function where in if computer plays first use a custom funtion where in it plays double win method

'''


ob=tictactoe()
ob.play()
