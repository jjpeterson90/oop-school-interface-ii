from tkinter import Menu
from classes.school import School

school = School('Ridgemont High')

menu_prompt = "\nWhat would you like to do?\nOptions:\n1. List All Students\n2. View Individual Student <student_id>\n3. Add a Student\n4. Remove a Student <student_id>\n5. Quit\n"

# mode = input(menu_prompt)

while True:
    mode = input(menu_prompt)
    if mode == '1':
        school.list_students()
    elif mode == '2':
        student_id = input('Enter a student id:')
        school.find_student_by_id(student_id)
    elif mode == '5':
        break

# print(school.staff)
# print(school.students)
