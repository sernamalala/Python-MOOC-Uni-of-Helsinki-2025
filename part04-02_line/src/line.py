# Write your solution here
def line(num,string):
    if string!="":
        print(num*string[0])
    else:
        string="*"
        print(num*string)
# You can test your function by calling it within the following block
if __name__ == "__main__":
    line(5, "xxx")