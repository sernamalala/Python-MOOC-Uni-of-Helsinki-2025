# Write your solution here
def everything_reversed(array):
    word = ""
    new_array = []
    for i in range(len(array)-1,-1,-1):
        for j in range(len(array[i])-1,-1,-1):
            print(array[i][j],end="")
            word+=array[i][j]
        print("")
        new_array.append(word)
        word = ""
    return new_array
