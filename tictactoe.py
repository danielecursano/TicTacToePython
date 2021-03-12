import random

class Game:
    """
    Author : RaffoBaffoBuffo
    Tic Tac Toe on terminal

    To start a new game:
        args: p1 = str(name of player 1)
              p2 = str(name of player 2)

        new_game = Game(p1, p2)

        and the game will start

        ex: 
            p1 = input('Player 1 insert name: ')
            p2 = input('Player 2 insert name: ')
            new = Game(p1, p2)

    """
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.boxPlayed = {p1: [], p2: []}
        self.start()

    def checkBox(self, box):
        """
        First if statement checks if the n. box played is valid 
        The box are called with numbers from 1 to 9

        Then check if the box is already occupied
        If true the user is asked to play another box

        """

        if box in range(9):
            if box not in self.boxPlayed[self.p1] and box not in self.boxPlayed[self.p2]:
                return True
        return False

    def draw(self):
        """
        Once the input is validated the game draws the player's
        symbol in the chosen box

        This function returns a list with the symbol played at its index

        """

        board = []
        box = self.boxPlayed
        for i in range(9):
            if i in box[self.p1]:
                board.insert(i, 'x')
            elif i in box[self.p2]:
                board.insert(i, 'o')
            else:
                board.insert(i, ' ')
        return board

    def checkWin(self):
        """
        Ugly if statements to check if someone win or not
        """

        board = self.draw()
        if board[0]==board[1]==board[2] != ' ':
            return False
        elif board[3]==board[4]==board[5] != ' ':
            return False
        elif board[6]==board[7]==board[8] != ' ':
            return False
        elif board[0]==board[3]==board[6] != ' ':
            return False
        elif board[1]==board[4]==board[7] != ' ':
            return False
        elif board[2]==board[5]==board[8] != ' ':
            return False
        elif board[0]==board[4]==board[8] != ' ':
            return False
        elif board[2]==board[4]==board[6] != ' ':
            return False
        return True

    def play(self, box, player):
        """
        The input is checked and if the box is already used it returns False
        to ask a new input
        If not the list with the values is printed and the game passes to
        the other opponent

        """
        if self.checkBox(box):
            self.boxPlayed[player].append(box)
            board = self.draw()
            for k in range(len(board)):
                if board[k] == 'x':
                    board[k] = '\U0000274C'
                if board[k] == 'o':
                    board[k] = '\U00002B55'
                if board[k] == ' ':
                    board[k] = '\U000025FE'
            for i in range(len(board)):
                print(board[i], end=' ')
                if i in (2, 5, 8):
                    print()
            print('------------------------')
            return True
        else:
            print('Box already occupied')
            return False

    def start(self):
        """
        Main function in which the game asks for the input, 
        plays the box and if: all the boxes are written but the function Game.checkWin()
        doesn't return anything it's draw
        else: 
            the while loop stops when Game.checkWin() returns False
            so the winner is the one who played as last

        Line 143 the program prints player[not i] because in line 134
        there is already the pass from the one who played and the next player
        """

        players = [self.p1, self.p2]
        i = random.randint(0, 1)
        while self.checkWin():
            inputP = input('{} type box: '.format(players[i]))
            while True:
                try:
                    inputP = int(inputP)
                    inputP -= 1
                    break
                except:
                    inputP = input('Type valid box (1-9):')

            if self.play(int(inputP), players[i]):
                i = not i

            else:
                pass

            if len(self.boxPlayed[self.p1]+self.boxPlayed[self.p2]) == 9:
                message = 'DRAW'
                break

            message = '{} WINS'.format(players[not i])

        print(message) 
