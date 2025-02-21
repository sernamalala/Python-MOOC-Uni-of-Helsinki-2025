# Write your solution here

items_no = int(input("How many items:"))
my_list = []
for i in range(items_no):
    current_item = int(input(f"Item {i+1}:"))
    my_list.append(current_item)
print(my_list)
