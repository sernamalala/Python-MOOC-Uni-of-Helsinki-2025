# Write your solution here

def create_tuple(x: int, y: int, z: int):
    tup = (x,y,z)

    result = (min(tup), max(tup),sum(tup))

    return result
