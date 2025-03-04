# Write your solution here

def play_turn(game_board: list, x: int, y: int, piece: str):

    for i in range(len(game_board)):
        if x > len(game_board)-1 or y>len(game_board)-1 or x<0 or y<0:
            return False
        if i == y:
            for j in range(len(game_board[i])):

                if j==x:
                    if game_board[i][j] == "":
                        game_board[i][j] = piece
                        return True
                    else:
                        return False
                

