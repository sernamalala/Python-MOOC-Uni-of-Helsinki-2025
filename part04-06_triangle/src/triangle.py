# Copy here code of line function from previous exercise
def line(num,string):
    if string!="":
        print(num*string[0])
    else:
        string="*"
        print(num*string)
def triangle(size):
    # You should call function line here with proper parameters
    hashes = 1
    for i in range(size):
        line(hashes, "#")
        hashes+=1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)
