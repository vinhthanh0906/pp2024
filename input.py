from domain import Student, Course
from data import students, courses

def input_number_of_students():
    return int(input("Enter the number of students in the class: "))

def input_student_information():
    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")
    dob = input("Enter student date of birth (DoB): ")
    students.append(Student(student_id, name, dob))

def input_number_of_courses():
    return int(input("Enter the number of courses: "))

def input_course_information():
    course_id = input("Enter course ID: ")
    name = input("Enter course name: ")
    courses.append(Course(course_id, name))

def input_marks_for_course():
    course_id = input("Enter course ID to input marks: ")
    for course in courses:
        if course.course_id == course_id:
            print(f"Entering marks for course: {course.name}")
            for student in students:
                mark = float(input(f"Enter marks for {student.name} (ID: {student.student_id}): "))
                student.marks[course_id] = mark
            return
    print("Course not found!")
