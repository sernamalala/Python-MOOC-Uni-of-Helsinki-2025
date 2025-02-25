# Write your solution here

def longest_series_of_neighbours(my_list):
    if not my_list:
        return 0
    
    count = 1
    max_count = 1

    for i in range(1,len(my_list)):
        if abs(my_list[i] - my_list[i-1]) == 1:
            count+=1
        else:
            max_count = max(max_count,count)
            count = 1
    max_count = max(max_count,count)
    return max_count
