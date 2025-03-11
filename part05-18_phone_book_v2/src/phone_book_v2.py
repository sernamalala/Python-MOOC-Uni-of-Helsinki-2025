# Write your solution here# Write your solution here
phonebook = {}
number_list = []
while True:
    
    command = int(input("command (1 search, 2 add, 3 quit):"))

    if command == 3:
        print("quitting...")
        break
    elif command == 2:
        name = input("name: ")
        number = input("number: ")
        
        if name in phonebook:
            phonebook[name].append(number)
        else:
            phonebook[name] = [number]
       
        print("ok!")
    elif command == 1:
        name = input("name: ")
        if name in phonebook:
            for i in phonebook[name]:
                print(i)
        else:
            print("no number")

    