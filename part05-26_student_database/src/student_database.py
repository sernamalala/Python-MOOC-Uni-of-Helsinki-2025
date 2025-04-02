# Write your solution here

students = []

def add_student(database, name):
    my_student = {}
    my_student["name"] = name
    my_student["completed_course"] = []
    database.append(my_student)


def print_student(database, name):
    
    for student in students:
        print(name+":   ")

        if(student["name"] == name):
            if(len(student["completed_course"])>0):
                print(f" {student["completed_course"]}")
            else:
                print("no completed course")
        elif (student["name"] != name):
            print("no such person in the database")


add_student(students, "Peter")
add_student(students, "Eliza")
print_student(students, "Peter")
print_student(students, "Eliza")
print_student(students, "Jack")