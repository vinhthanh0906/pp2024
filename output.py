from data import students, courses

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

def calculate_gpa(student):
    if not student.marks:
        return 0.0
    total_marks = sum(student.marks.values())
    num_courses = len(student.marks)
    return total_marks / num_courses
def calculate_gpa(student):
    if not student.marks:
        return 0.0
    total_marks = sum(student.marks.values())
    num_courses = len(student.marks)
    return total_marks / num_courses
