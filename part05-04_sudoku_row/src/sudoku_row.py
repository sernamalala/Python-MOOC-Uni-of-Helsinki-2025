# Write your solution here

def row_correct(sudoku: list, row_no: int):
    current_row = []
    for row in range(len(sudoku)):
        if row == row_no:
            for i in sudoku[row]:
                current_row.append(i)
    vals = [1,2,3,4,5,6,7,8,9]

    counts = []
    for val in vals:
        counts.append(current_row.count(val))
    
    print(counts)
    
    allowed = [0,1]
    for val in counts:
        if val not in allowed:
            return False
        
    return True
    