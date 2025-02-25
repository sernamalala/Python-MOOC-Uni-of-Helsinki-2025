# Write your solution here

def no_shouting(my_list):
    new_list = []
    for i in my_list:
        if i.isupper() == False:
            new_list.append(i)
    return new_list

