# Write your solution here

def anagrams(word1,word2):
    sorted_word1 = sorted(word1)
    sorted_word2 = sorted(word2)

    if(sorted_word1==sorted_word2):
        return True
    else:
        return False
