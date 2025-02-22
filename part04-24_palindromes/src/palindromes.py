# Write your solution here
# Note, that at this time the main program should not be written inside
# if __name__ == "__main__":
# block!

def palindromes(word):
    check = ""
    for i in range(len(word)-1,-1,-1):
        check+=word[i]

    if check==word:
        return True
    else:
        return False
            

while True:
    word = input("Please type in a palindrome:")
    
    if palindromes(word):
        print(f"{word} is a palindrome!")
        break

        
    else:
        print("that wasn't a palindrome")
        

