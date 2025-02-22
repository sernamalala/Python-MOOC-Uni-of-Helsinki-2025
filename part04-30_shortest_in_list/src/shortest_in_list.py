# Write your solution here

def shortest(my_list):
    shortest = my_list[0]

    for i in range(len(my_list)):
        if len(my_list[i])<=len(shortest):
            shortest = my_list[i]
    return shortest
