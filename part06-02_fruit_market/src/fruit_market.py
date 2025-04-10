# write your solution here

def read_fruits():
    fruits_dict = {}
    with open('src/fruits.csv') as fruits_files:
        for line in fruits_files:
            info = line.split(";")
            fruits_dict[info[0]] = float(info[1])

    return fruits_dict

