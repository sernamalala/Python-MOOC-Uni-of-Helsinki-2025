# Write your solution here
def longest(strings: list):
    longest = 0
    longest_word = ""
    for word in strings:
        
        if len(word)>longest:
            longest = len(word)
            longest_word = word
    return longest_word
