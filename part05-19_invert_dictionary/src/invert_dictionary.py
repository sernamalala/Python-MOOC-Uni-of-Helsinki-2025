# Write your solution here

def invert(dictionary: dict):
    temp = dictionary.copy()
    dictionary.clear()
    for key in temp:
        my_key = key
        my_val = temp[key]
        dictionary[my_val] = my_key

