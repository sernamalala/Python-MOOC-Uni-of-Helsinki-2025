# Write your solution here
def greatest_number(a,b,c):
    if a>=b and a>=c:
        return a
    elif c>=b and c>=a:
        return c
    elif b>=a and b>=c:
        return b
    elif a==b==c:
        return a
# You can test your function by calling it within the following block
if __name__ == "__main__":
    greatest = greatest_number(5, 4, 8)
    print(greatest)