# Write your solution here

def factorials(n: int):
    my_values = {}
    val = 1
    for i in range(1,n+1):
        val *=i
        my_values[i] = val
    return my_values
    