# Write your solution here

def block_correct(sudoku: list, row_no: int, column_no: int):
    block = []
    counts = []
    index_row = row_no
    for row in range(len(sudoku)):
        if row<=index_row+2 and row>=row_no:
            for i in range(column_no, column_no+3):
                # print(sudoku[row][i],end="")
                block.append(sudoku[row][i])
            
        
    vals = [1,2,3,4,5,6,7,8,9]
    
    
    for val in vals:
        counts.append(block.count(val))
        

    allowed = [0,1]
    for count in counts:
        if count not in allowed:
            return False
        
    return True
        


 