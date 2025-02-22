# Write your solution here
array = []
num = 1
while True:
    print(f"The list is now {array}")
    input_command = input("a(d)d, (r)emove or e(x)it:")

    if input_command == "d":
        array.append(num)
        num+=1
    elif input_command == "r":
        array.pop()
        num-=1
    if input_command == "x":
        print("Bye!")
        break
        
    


    
    