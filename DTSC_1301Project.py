# Project question:
# How do average GPA and stress differ among students with different sleep hours?

import csv

# STEP 1: Open the CSV file.
# Keep the CSV in the same folder and run this program from that folder.
file = open("college_student_sleep_academic_performance.csv", "r")
reader = csv.DictReader(file)

# STEP 2: Store the students in a list of dictionaries.
# Each dictionary contains one student's information.
students = []

for row in reader:
    students.append(row)

file.close()

# STEP 3: Create three groups based on sleep hours.
# These groups are just for comparing the data.
low_sleep = []
medium_sleep = []
high_sleep = []

for student in students:
    # CSV values start as text. float() changes text to a decimal number.
    sleep = float(student["Sleep_Hours"])

    if sleep < 6:
        low_sleep.append(student)
    elif sleep < 8:
        medium_sleep.append(student)
    else:
        high_sleep.append(student)

# Put the group names and lists into a dictionary.
sleep_groups = {
    "Under 6 hours": low_sleep,
    "6 to under 8 hours": medium_sleep,
    "8 hours or more": high_sleep
}

# STEP 4: Calculate and print the averages for each group.
print("SLEEP, GPA, AND STRESS")
print("Total students:", len(students))

for group_name in sleep_groups:
    group = sleep_groups[group_name]
    total_gpa = 0
    total_stress = 0

    for student in group:
        total_gpa = total_gpa + float(student["GPA"])
        total_stress = total_stress + float(student["Stress_Level"])

    number_of_students = len(group)

    print()
    print("Sleep group:", group_name)
    print("Number of students:", number_of_students)

    # Check for an empty group so we do not divide by zero.
    if number_of_students > 0:
        average_gpa = total_gpa / number_of_students
        average_stress = total_stress / number_of_students

        print("Average GPA:", round(average_gpa, 2))
        print("Average stress:", round(average_stress, 2))
    else:
        print("No students in this group.")

print()
print("These results describe synthetic data, not real student findings.")
print("They do not prove that sleep causes GPA or stress to change.")
print("Stress uses the original dataset scale, whose endpoints are not defined.")
