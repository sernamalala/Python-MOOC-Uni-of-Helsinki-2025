# Write your solution here

def transpose(matrix: list):
    
    trans_matrix = []

    for i in range(len(matrix[0])):
        matrix_rows = []

        for row in matrix:
            matrix_rows.append(row[i])

        trans_matrix.append(matrix_rows)
    
    matrix.clear()
    for row in trans_matrix:
        matrix.append(row) 


m = [[1, 2 ,3],[4, 5, 6],[7, 8, 9]]

print(transpose(m))