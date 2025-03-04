# Write your solution here

def double_items(numbers: list):
    list_copy = numbers[:]

    double_list = []
    for i in list_copy:
        double_list.append(i*2)
    return double_list
