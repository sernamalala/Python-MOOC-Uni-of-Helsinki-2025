# Write your solution here



def no_vowels(string):
    vowels = ['a','e','i','o','u']
    new_string = ""
    for i in range(len(string)):
        if(string[i] not in vowels):
            new_string+=string[i]
    return new_string
