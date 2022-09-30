
###########################################################################################################################
#                                                    EXERCISE 5.1
###########################################################################################################################

# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

# 🚨 Don't change the code above 👆

#Write your code below this row 👇

#print(student_heights)
#print(sum(student_heights))
#print(len(student_heights))

total_height = 0

for height in student_heights:
    total_height += height

no_of_students = 0

for student in student_heights:
    no_of_students += 1

average_height = round(total_height / no_of_students)
print(f"Average Height os Students is : {average_height}")