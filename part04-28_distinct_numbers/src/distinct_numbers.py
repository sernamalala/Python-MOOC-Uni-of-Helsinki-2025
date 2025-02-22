# Write your solution here

def distinct_numbers(my_list):
    new_list = []

    for i in range(len(my_list)):
        if my_list[i] not in new_list:
            new_list.append(my_list[i])
    new_list.sort()
    return new_list
