# Write your solution here

array = []
while True:
    word = input("Word: ")
    if word not in array:
        array.append(word)
    else:
        print(f"You typed in {len(array)} different words")
        break

    
