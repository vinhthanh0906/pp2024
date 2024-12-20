from input import  input_number_of_students, input_student_information, input_number_of_courses, input_course_information, input_marks_for_course
from output import list_courses, list_students, show_student_marks_for_course, calculate_gpa
from data import students, courses



#Choose a number match to the function you want to use
def main():
    while True:
        print("\n--- Student Mark Management ---")
        print("1. Input number of students and their details")
        print("2. Input number of courses and their details")
        print("3. Input marks for a course")
        print("4. List all courses")
        print("5. List all students")
        print("6. Show student marks for a given course")
        print("7. Calculate GPA for a student")
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
        elif choice == "7":
            student_id = input("Enter the student ID to calculate GPA: ")
            student_obj = next((s for s in students if s.student_id == student_id), None)
            if student_obj:
                gpa = calculate_gpa(student_obj)
                print(f"GPA for {student_obj.name} (ID: {student_obj.student_id}): {gpa:.2f}")
            else:
                print("Student not found!")
        elif choice == "0":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
