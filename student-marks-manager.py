students = {
    "Aman": [85, 90, 78],
    "Riya": [92, 88, 95],
    "Zoya": [70, 65, 80]
}


# Function to calculate average
def calculate_average(marks):
    return round(sum(marks) / len(marks), 2)


# Function to calculate grade
def calculate_grade(average):
    if average >= 85:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 50:
        return "C"
    else:
        return "F"


# Function to display all students
def view_all_students():
    print("\n--- STUDENT MARKS ---")

    for name, marks in students.items():
        average = calculate_average(marks)
        grade = calculate_grade(average)

        print(name, average, grade)


# Function to find topper
def show_topper():
    topper = None
    highest_average = -1

    for name, marks in students.items():
        average = calculate_average(marks)

        if average > highest_average:
            highest_average = average
            topper = name

    if topper is not None:
        print("Topper:", topper)


# Function to add a student
def add_student():
    name = input("Enter student name: ").strip()

    if name in students:
        print("Student already exists.")
        return

    while True:
        marks = []
        valid = True

        for i in range(1, 4):
            mark = int(input(f"Enter mark {i}: "))

            if mark < 0 or mark > 100:
                print("Invalid mark, try again.")
                valid = False
                break

            marks.append(mark)

        if valid:
            students[name] = marks
            print("Student added successfully.")
            break


# Stage 4: Menu
while True:
    print("\n--- STUDENT MARKS MANAGER ---")
    print("1. Add student")
    print("2. View all")
    print("3. Show topper")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_all_students()

    elif choice == "3":
        show_topper()

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")
