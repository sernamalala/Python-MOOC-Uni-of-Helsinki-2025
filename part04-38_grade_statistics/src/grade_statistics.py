# Write your solution here
import math
exam_points_marks = []
while True:
    exam_points = input("Exam points and exercises completed:")
    if exam_points=="":
        break
    exam_points_marks.append(exam_points)

print("Statistics:")
points = []
pass_count = 0
exam_marks_list = []
for i in exam_points_marks:
    val = i.split(" ")
    exam_marks = float(val[0])
    exam_marks_list.append(exam_marks)
    final = exam_marks + math.floor(int(val[1])/10)
    if exam_marks>=10 and final>=15:
        pass_count+=1
    points.append(final)

# print(points)
total = 0
count = 0
for i in points:
    total +=i
    count+=1

average = total/count
percent = (pass_count/count) * 100
print(f"Points average: {average:.1f}")
print(f"Pass percentage: {percent:.1f}")

grades = []
for i in range(len(points)):
    if exam_marks_list[i]<10 or points[i]<=14:
        grades.append(0)

    elif points[i]>=15 and points[i]<=17 and exam_marks_list[i]>=10:
        grades.append(1)

    elif points[i]>=18 and points[i]<=20 and exam_marks_list[i]>=10:
        grades.append(2)
    
    elif points[i]>=21 and points[i]<=23 and exam_marks_list[i]>=10:
        grades.append(3)

    elif points[i]>=24 and points[i]<=27 and exam_marks_list[i]>=10:
        grades.append(4)

    elif points[i]>=28 and points[i]<=30 and exam_marks_list[i]>=10:
        grades.append(5)

print("Grade distribution:")

for i in range(5,-1,-1):
    grade_count = grades.count(i)
    print(f"    {i}: {"*"* grade_count}")
    
