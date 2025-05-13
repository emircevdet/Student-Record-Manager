from database import create_table
from functions import add_student, update_student, delete_student, list_students

def main_menu():
    create_table()
    while True:
        print("\n--- Student Record Manager ---")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. List All Students")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            name = input("Name: ")
            number = input("Student Number: ")
            department = input("Department: ")
            try:
                gpa = float(input("GPA: "))
                add_student(name, number, department, gpa)
                print("Student added successfully.")
            except ValueError:
                print("GPA must be a number.")

        elif choice == '2':
            number = input("Student Number to update: ")
            name = input("New Name: ")
            department = input("New Department: ")
            try:
                gpa = float(input("New GPA: "))
                update_student(number, name, department, gpa)
                print("Student updated successfully.")
            except ValueError:
                print("GPA must be a number.")

        elif choice == '3':
            number = input("Student Number to delete: ")
            delete_student(number)
            print("Student deleted.")

        elif choice == '4':
            students = list_students()
            if not students:
                print("No student records found.")
            else:
                print("\n--- Student List ---")
                for s in students:
                    print(f"ID: {s[0]} | Name: {s[1]} | Number: {s[2]} | Department: {s[3]} | GPA: {s[4]}")

        elif choice == '5':
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()

