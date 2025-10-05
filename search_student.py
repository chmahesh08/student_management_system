def search_student(students):
    if not students:
        print("\nNo students to search.\n")
        return

    keyword = input("Enter Student ID or Name to search: ").strip()
    found = False
    for s in students:
        if str(s["id"]) == keyword or s["name"].lower() == keyword.lower():
            print(f"\nFound Student:")
            print(f"ID: {s['id']}, Name: {s['name']}, Course: {s['course']}, Marks: {s['marks']}\n")
            found = True
            break

    if not found:
        print("\n Student not found.\n")
