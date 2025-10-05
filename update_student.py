def update_student(students):
    if not students:
        print("\nNo students available to update.\n")
        return

    try:
        sid = int(input("Enter Student ID to update: "))
    except ValueError:
        print("Invalid ID! Please enter a number.")
        return

    for student in students:
        if student["id"] == sid:
            print(f"\nFound Student: {student['name']} ({student['course']}) - Marks: {student['marks']}")
            print("1. Update Course")
            print("2. Update Marks")
            choice = input("Enter your choice (1/2): ")

            if choice == "1":
                new_course = input("Enter new course (CS/ECE/IT/MECH/CIVIL): ").upper()
                if new_course in ["CS", "ECE", "IT", "MECH", "CIVIL"]:
                    student["course"] = new_course
                    print("\n Course updated successfully!\n")
                else:
                    print("\n Invalid course name!\n")

            elif choice == "2":
                try:
                    new_marks = int(input("Enter new marks (0–100): "))
                    if 0 <= new_marks <= 100:
                        student["marks"] = new_marks
                        print("\n Marks updated successfully!\n")
                    else:
                        print("\n Marks should be between 0–100.\n")
                except ValueError:
                    print("\n Invalid marks input!\n")
            else:
                print("\n Invalid choice!\n")
            return

    print("\n Student not found!\n")
