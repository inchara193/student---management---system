import json

FILE = "students.json"

# Load data
def load_data():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        return []

# Save data
def save_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f)

# Add student
def add_student():
    name = input("Enter name: ")
    age = input("Enter age: ")
    student = {"name": name, "age": age}

    data = load_data()
    data.append(student)
    save_data(data)
    print("Student added!")

# View students
def view_students():
    data = load_data()
    if not data:
        print("No students found")
    else:
        for i, s in enumerate(data):
            print(i, s)

# Delete student
def delete_student():
    data = load_data()
    view_students()
    index = int(input("Enter index to delete: "))
    
    if 0 <= index < len(data):
        data.pop(index)
        save_data(data)
        print("Deleted successfully")
    else:
        print("Invalid index")

# Menu
while True:
    print("\n1. Add Student\n2. View Students\n3. Delete Student\n4. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        delete_student()
    elif choice == "4":
        break
    else:
        print("Invalid choice")
