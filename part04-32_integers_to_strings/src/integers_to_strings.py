# Write your solution here

def formatted(my_list): 
    new_list = []
    for i in range(len(my_list)):
        new_list.append(f"{my_list[i]:.2f}")
    return new_list
