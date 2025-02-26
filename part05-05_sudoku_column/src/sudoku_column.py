# Write your solution here

def column_correct(sudoku: list, column_no: int):
    current_col = []
    for row in sudoku:
        current_col.append(row[column_no])
            
    vals = [1,2,3,4,5,6,7,8,9]

    counts = []
    for val in vals:
        counts.append(current_col.count(val))
    
    allowed = [0,1]
    for val in counts:
        if val not in allowed:
            return False
        
    return True
    
