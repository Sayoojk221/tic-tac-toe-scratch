#Tic Tac Toe Game Design
board =[
    ['_','_','_'],
    ['_','_','_'],
    ['_','_','_']
]

board_number = {'1':[0,0],'2':[0,1],'3':[0,2],'4':[1,0],'5':[1,1],'6':[1,2],
                '7':[2,0],'8':[2,1],'9':[2,2]}

for i in range(3):
        for j in range(3):
            print(board[i][j],end='     ')
        print('\n')
        print('')

#player value add(X,O)
def data_insertion(item,Value):
    
    if Value == 'X':
        list = board_number[item]
        board[list[0]][list[1]]=Value
    elif Value == 'O':
        list = board_number[item]
        board[list[0]][list[1]]=Value
    for i in range(3):
        for j in range(3):
            print(board[i][j],end='     ')
        print('\n')
        print('')
    game_stop = winner_check()
    return game_stop
    

#To check Winner
def winner_check():
    for i in range(3):
        j = 0
        if board[i][j] == 'X' and board[i][j+1] == 'X' and board[i][j+2] == 'X':
            print('Winner A')
            flag=1
            return flag
        elif board[i][j] == 'O' and board[i][j+1] == 'O' and board[i][j+2] == 'O':
            print('Winner B')
            flag=1
            return flag
    for j in range(3):
        i = 0 
        if board[i][j] == 'X' and board[i+1][j] == 'X' and board[i+2][j] == 'X':
            print('Winner A')
            flag=1
            return flag
        elif board[i][j] == 'O' and board[i+1][j] == 'O' and board[i+2][j] == 'O':
            print('Winner B')
            flag=1
            return flag
    if True:
        if board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X':
            print('Winner A')
            flag=1
            return flag
        elif board[0][2] == 'X' and board[1][1] == 'X' and board[2][0] == 'X':
            print('Winner A')
            flag=1
            return flag
        elif board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O':
            print('Winner B')
            flag=1
            return flag
        elif board[0][2] == 'O' and board[1][1] == 'O' and board[2][0] == 'O':
            print('Winner B')
            flag=1
            return flag
    
    
#Draw checking function
def game_draw():
    count = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'X' or board[i][j] == 'O' :
                count += 1
    return count 



#Players Option(A,B)

def game_start():
    Player_A = True
    Player_B = False
    for Player_Selection in range(100):
        draw_value = game_draw()
        if draw_value == 9:
            print('A & B Draw!')
            break
        elif Player_A == True:
            print('Player A')
            value_A = 'X'
            user_entered_value = input('choose (1-9): ')
            list = board_number[user_entered_value]
            if board[list[0]][list[1]] == '_':
                game_stop = data_insertion(user_entered_value,value_A)
                if game_stop == 1:
                    break
                Player_A = False
                Player_B = True
            else:
                print('location have value')

        elif Player_B == True:
            print('Player B')
            value_B = 'O'
            user_entered_value = input('choose (1-9): ')
            list = board_number[user_entered_value]
            if board[list[0]][list[1]] == '_':
                game_stop = data_insertion(user_entered_value,value_B)
                if game_stop == 1:
                    break
                Player_A = True
                Player_B = False
            else:
                print('location have value')

game_start()