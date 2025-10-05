def delete_student(students):
    if not students:
        print("\nNo students to delete.\n")
        return

    try:
        sid = int(input("Enter Student ID to delete: "))
    except ValueError:
        print("Invalid ID! Please enter a number.\n")
        return

    for s in students:
        if s["id"] == sid:
            students.remove(s)
            print(f"\n Student '{s['name']}' deleted successfully!\n")
            return

    print("\n Student not found.\n")
