# Write your solution here

def dict_of_numbers():
    current = ""
    my_numbers = {0:"zero",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine", 10:"ten", 20:"twenty",30:"thirty",40:"forty",50:"fifty",60:"sixty",70:"seventy",80:"eighty",90:"ninety"}

    for input_val in range(11,100):

        if input_val>10 and input_val<=99:

            new_i = int(str(input_val)[0]+"0")
            current+=my_numbers[new_i]
            current+="-"
            val2 = int(str(input_val)[1])
            current+=my_numbers[val2]
            my_numbers[new_i] =current
    return my_numbers
        
        

numbers = dict_of_numbers()
print(numbers[2])
print(numbers[11])
print(numbers[45])
print(numbers[99])
print(numbers[0])