# Write your solution here

def list_sum(list1,list2):
    new_list = []

    for i in range(len(list1)):
        num = list1[i]+list2[i]
        new_list.append(num)
    return new_list

