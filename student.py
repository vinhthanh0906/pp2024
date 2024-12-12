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

# Data storage
students = []
courses = []

# Input functions
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

# Listing functions
def list_courses():
    print("\nCourses:")
    for course in courses:
        print(f"{course.course_id} - {course.name}")

def list_students():
    print("\nStudents:")
    for student in students:
        print(f"{student.student_id} - {student.name}, DoB: {student.dob}")

def show_student_marks_for_course():
    course_id = input("Enter course ID to display marks: ")
    for course in courses:
        if course.course_id == course_id:
            print(f"\nMarks for course: {course.name}")
            for student in students:
                mark = student.marks.get(course_id, "N/A")
                print(f"{student.name} (ID: {student.student_id}): {mark}")
            return
    print("Course not found!")

# Main program
def main():
    while True:
        print("\n--- Student Mark Management ---")
        print("1. Input number of students and their details")
        print("2. Input number of courses and their details")
        print("3. Input marks for a course")
        print("4. List all courses")
        print("5. List all students")
        print("6. Show student marks for a given course")
        print("0. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            num_students = input_number_of_students()
            for _ in range(num_students):
                input_student_information()
        elif choice == "2":
            num_courses = input_number_of_courses()
            for _ in range(num_courses):
                input_course_information()
        elif choice == "3":
            input_marks_for_course()
        elif choice == "4":
            list_courses()
        elif choice == "5":
            list_students()
        elif choice == "6":
            show_student_marks_for_course()
        elif choice == "0":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()