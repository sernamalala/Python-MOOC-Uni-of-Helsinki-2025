# Write your solution here

def histogram(string: str):
    occurences = {}
    unique_values = set(string)
    for i in unique_values:
        occurences[i] = string.count(i)
    
    for key in occurences:
        print(f"{key} {"*"*occurences[key]}")

