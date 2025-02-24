# Write your solution here

def most_common_character(string):
    highest = 0

    for i in range(len(string)):
        count = string.count(string[i])
        if count>highest:
            highest=count
            char = string[i]
    return  char       
