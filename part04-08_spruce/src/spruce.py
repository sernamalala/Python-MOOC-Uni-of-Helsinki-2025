# Write your solution here
def spruce(num):
    numbers = []
    print("a spruce!")
    white_space = " "
    count = 1
    for i in range(num):
        print(f"{int((((num*2)-1)-count)/2)*white_space}",end="")
        print(f"{count*"*"}")
        count+=2
    count = 1
    print(f"{int((((num*2)-1)-count)/2)*white_space}",end="")
    print(f"{count*"*"}")

# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(5)