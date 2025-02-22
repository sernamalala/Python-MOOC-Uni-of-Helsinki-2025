# Write your solution here

def sum_of_positives(my_list):
    add = 0
    for i in range(len(my_list)):
        if my_list[i]>0:
            add+=my_list[i]
    return add


