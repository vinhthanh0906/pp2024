from domain import Student, Course
from data import students, courses

def input_number_of_students():
    return int(input("Enter the number of students in the class: "))

def input_student_information():
    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")
    dob = input("Enter student date of birth (DoB): ")
    students.append(Student(student_id, name, dob)) # Make a new Student object with attribute, then add it into students list

def input_number_of_courses():
    return int(input("Enter the number of courses: "))

def input_course_information():
    course_id = input("Enter course ID: ") #input Id
    name = input("Enter course name: ") #input name
    courses.append(Course(course_id, name)) # add the Course object to course list

def input_marks_for_course():
    course_id = input("Enter course ID to input marks: ")
    for course in courses:  # run loop through courses list
        if course.course_id == course_id:# Checking if the course_id exist in the list
            print(f"Entering marks for course: {course.name}") # if yes, print course's name 
            for student in students:
                mark = float(input(f"Enter marks for {student.name} (ID: {student.student_id}): ")) #input the mark
                student.marks[course_id] = mark
            return
    print("Course not found!")
