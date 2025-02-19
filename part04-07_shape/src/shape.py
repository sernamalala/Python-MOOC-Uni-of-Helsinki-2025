# Copy here code of line function from previous exercise and use it in your solution
def line(num,string):
    if string!="":
        print(num*string[0])
    else:
        string="*"
        print(num*string)
# You can test your function by calling it within the following block
def shape(triangle_num,triangle_character,square_num,square_character):
    triangle_piece = 1
    for i in range(triangle_num):
        line(triangle_piece,triangle_character)
        triangle_piece+=1
    for j in range(square_num):
        line(triangle_num,square_character)
if __name__ == "__main__":
    shape(5, "x", 2, "o")