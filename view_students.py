def view_students(students):
    if not students:
        print("\nNo students found.\n")
        return

    print("\n===== Student Records =====")
    print("{:<5} {:<15} {:<10} {:<6}".format("ID", "Name", "Course", "Marks"))
    print("-" * 40)
    for s in students:
        print("{:<5} {:<15} {:<10} {:<6}".format(s["id"], s["name"], s["course"], s["marks"]))
    print()
