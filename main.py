from add_student import add_student
from view_students import view_students
from search_student import search_student
from update_student import update_student
from delete_student import delete_student

students = []

def menu():
    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            update_student(students)
        elif choice == "5":
            delete_student(students)
        elif choice == "6":
            print("\n Exiting Student Management System. Goodbye!\n")
            break
        else:
            print("\n Invalid choice! Please try again.\n")

if __name__ == "__main__":
    menu()
