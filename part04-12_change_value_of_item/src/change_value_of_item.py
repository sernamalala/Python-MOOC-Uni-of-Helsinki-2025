# Write your solution here

array = [1, 2, 3, 4, 5]

while True:
    index = int(input("Index:"))
    
    if index==-1:
        break
    
    elif index>=0:
        new_value = int(input("New value:"))
        array[index] = new_value
    elif index<0:
        new_value = int(input("New value:"))
        array.append(new_value)
    
    print(array)
