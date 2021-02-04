##Printing the Tic Tac Toe Board ###
### The Board resembles the keyboard number position:###

Board = {'7':' ' , '8' : ' ' , '9':' ','4':' ','5':' ','6':' ', '1':' ' , '2': ' ' ,'3':' '}

def printboard(Board):

    print(f" {Board['7']} | {Board['8']} | {Board['9']}")
    print("---+---+---")
    print(f" {Board['4']} | {Board['5']} | {Board['6']}")
    print("---+---+---")
    print(f" {Board['1']} | {Board['2']} | {Board['3']}")

board_keys = []

for key in Board:
    board_keys.append(key)

#part 2:Build the game          

def game():

    turn = 'X'
    count = 0


    for i in range(10):
        printboard(Board)
        print(f"Its your turn {turn} ,What is your position number?")
        move = input()

        print("This is board move"+ Board[move])

        if Board[move] == ' ':
            Board[move] = turn
            count += 1
        else:
            print("The position is already filled, \n what is your move "+ turn +" ?")
            continue

# The winning condition has 8 possible rows and columns and diagnals. 
# we will check all the 8 conditions after 5 iterations and declare the user who played last.

        if count >= 5 :

            if Board['7'] == Board['8'] == Board['9'] != ' ': #top row
                printboard(Board)
                print("The winner is " + turn)
                break  

            elif Board['4'] == Board['5'] == Board['6'] != ' ': #second row
                printboard(Board)
                print("The winner is "+ turn)
                break 

            elif Board['1'] == Board['2'] == Board['3'] != ' ': # last row
                printboard(Board)
                print("The winner is " + turn)
                break 

            elif Board['7'] == Board['4'] == Board['1'] != ' ': # First Column
                printboard(Board)
                print("The winner is " + turn)
                break 

            elif Board['8'] == Board['5'] == Board['2'] != ' ': # Second Column
                printboard(Board)
                print("The winner is " + turn)
                break 

            elif Board['9'] == Board['6'] == Board['3'] != ' ': # Third Column
                printboard(Board)
                print("The winner is "+ turn)
                break 

            elif Board['7'] == Board['5'] == Board['3'] != ' ': # Diagnal 1
                printboard(Board)
                print("The winner is " + turn)
                break 

            elif Board['9'] == Board['5'] == Board['1'] != ' ': # Diagnal 2
                printboard(Board)
                print("The winner is " +  turn)
                break 

    
        if count == 9 and :
            print("***********Game Over*********")
            print("Its a Tie!")
            break
    
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'




#Ask the user for if they want to restart a new game



    restart = input("Do you want to restart the game 'Y' or 'N' ?")
    if restart == 'y' :
        for key in board_keys:
            Board[key] = ' '
        
        game()


if __name__ == "__main__":
    game()

          




                        


