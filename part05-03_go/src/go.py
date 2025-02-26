# Write your solution here

def who_won(game_board: list):
    p1_count = 0
    p2_count = 0
    for row in game_board:
        for element in row:
            if element==1:
                p1_count+=1
            elif element ==2:
                p2_count+=1
    
    if p1_count>p2_count:
        return 1
    elif p1_count<p2_count:
        return 2
    if p1_count==p2_count:
        return 0
