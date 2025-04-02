# Write your solution here

def older_people(people: list, year: int):
    
    name_list = []

    for person in people:
        new_age = person[1]
        new_name = person[0]

        if new_age< year:
            name_list.append(new_name)

    return name_list
