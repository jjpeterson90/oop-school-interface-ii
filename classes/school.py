from classes.staff import Staff
from classes.student import Student

class School:
    def __init__(self, name):
        self.name = name
        self.staff = Staff.objects()
        self.students = Student.objects()

    def list_students(self):
        student_count = 1
        print("\n")
        for each_student in self.students:
            print(f"{student_count}. {each_student.name} {each_student.school_id}")
            student_count += 1
            
    def find_student_by_id(self, student_id):
        for each_student in self.students:
            if each_student.school_id == student_id:
                print(each_student)