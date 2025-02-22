# Write your solution here

array = []
while True:
    new_item = int(input("New item:"))
    if new_item!=0:
        array.append(new_item)
        print(f"The list now: {array}")
        print(f"The list in order: {sorted(array)}")

    elif new_item==0:
        print("Bye!")
        break