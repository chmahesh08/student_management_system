def add_student(students):
    if len(students) >= 8:
        print("\n Cannot add more students (limit reached 8).\n")
        return

    try:
        sid = int(input("Enter Student ID: "))
    except ValueError:
        print("Invalid ID! Please enter a number.\n")
        return

    for s in students:
        if s["id"] == sid:
            print("Student ID already exists!\n")
            return

    name = input("Enter Student Name: ").capitalize()
    course = input("Enter Course (CS/ECE/IT/MECH/CIVIL): ").upper()
    if course not in ["CS", "ECE", "IT", "MECH", "CIVIL"]:
        print("Invalid course name!\n")
        return

    try:
        marks = int(input("Enter Marks (0–100): "))
        if marks < 0 or marks > 100:
            print(" Marks should be between 0–100.\n")
            return
    except ValueError:
        print("Invalid marks input!\n")
        return

    students.append({"id": sid, "name": name, "course": course, "marks": marks})
    print(f"\n Student '{name}' added successfully!\n")
