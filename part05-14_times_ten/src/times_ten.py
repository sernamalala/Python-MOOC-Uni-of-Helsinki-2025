# Write your solution here

def  times_ten(start_index: int, end_index: int):
    my_values = {}
    for i in range(start_index,end_index+1):
        my_values[i] = i*10
    return my_values

