# Write your solution here

def all_the_longest(my_list):
    longest = ""
    new_list = []
    for i in range(len(my_list)):
        if len(my_list[i])>len(longest):
            longest = my_list[i]

    length = len(longest)

    for j in range(len(my_list)):
        if len(my_list[j])==length:
            new_list.append(my_list[j])
    return new_list

