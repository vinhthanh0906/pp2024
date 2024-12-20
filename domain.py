class Student:
    def __init__(self, student_id, name, dob):
        self.student_id = student_id
        self.name = name
        self.dob = dob
        self.marks = {}  # Dictionary to store marks for courses

class Course:
    def __init__(self, course_id, name):
        self.course_id = course_id
        self.name = name
