from database import create_connection

def add_student(name, student_number, department, gpa):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO students (name, student_number, department, gpa) VALUES (?, ?, ?, ?)",
        (name, student_number, department, gpa)
    )
    conn.commit()
    conn.close()

def update_student(student_number, name, department, gpa):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE students SET name=?, department=?, gpa=? WHERE student_number=?",
        (name, department, gpa, student_number)
    )
    conn.commit()
    conn.close()

def delete_student(student_number):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute(
        "DELETE FROM students WHERE student_number=?",
        (student_number,)
    )
    conn.commit()
    conn.close()

def list_students():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    conn.close()
    return students
