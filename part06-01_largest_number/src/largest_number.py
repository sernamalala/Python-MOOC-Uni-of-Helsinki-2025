# write your solution here

def largest():
    number = float("-inf")
    with open("numbers.txt") as numbers_file:
        for line in numbers_file:
            if int(line)>number:
                number = int(line)
    return number

