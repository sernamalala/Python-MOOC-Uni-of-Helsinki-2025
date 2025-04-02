# Write your solution here

def oldest_person(people: list):
    
    age = people[0][1]
    name = people[0][0]

    for person in people:
        new_age = person[1]
        new_name = person[0]

        if new_age< age:
            age = new_age
            name = new_name

    return name

