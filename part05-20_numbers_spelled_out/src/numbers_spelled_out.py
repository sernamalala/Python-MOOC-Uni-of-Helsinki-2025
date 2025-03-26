# Write your solution here

def dict_of_numbers():
    current = ""
    my_numbers = {
        0: "zero", 1: "one", 2: "two", 3: "three", 4: "four",
        5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine",
        10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen",
        15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen",
        20: "twenty", 30: "thirty", 40: "forty", 50: "fifty",
        60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety"
    }

    for input_val in range(21,100):
        tens = (input_val//10)*10
        ones = input_val %10

        if ones == 0:
            continue

        my_numbers[input_val] = my_numbers[tens] + "-" + my_numbers[ones]

    return my_numbers
        