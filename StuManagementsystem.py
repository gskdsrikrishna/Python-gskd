#Student Management System
class Student:
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number
        self.grades = {}
        self.attendance = {}

    def add_grade(self, subject, grade):
        self.grades[subject] = grade

    def add_attendance(self, date, status):
        self.attendance[date] = status

    def get_average_grade(self):
        if len(self.grades) == 0:
            return 0

        total_grade = sum(self.grades.values())
        return total_grade / len(self.grades)

    def get_attendance_percentage(self):
        if len(self.attendance) == 0:
            return 0

        total_days = len(self.attendance)
        present_days = list(self.attendance.values()).count("Present")
        return (present_days / total_days) * 100


class StudentManagementSystem:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def find_student(self, roll_number):
        for student in self.students:
            if student.roll_number == roll_number:
                return student
        return None

    def enroll_student(self):
        name = input("Enter student name: ")
        roll_number = input("Enter roll number: ")

        if self.find_student(roll_number):
            print("Student with roll number", roll_number, "already exists.")
            return

        student = Student(name, roll_number)
        self.add_student(student)
        print("Student enrolled successfully.")

    def add_grade(self):
        roll_number = input("Enter student's roll number: ")
        student = self.find_student(roll_number)

        if not student:
            print("Student with roll number", roll_number, "not found.")
            return

        subject = input("Enter subject name: ")
        grade = float(input("Enter grade: "))
        student.add_grade(subject, grade)
        print("Grade added successfully.")

    def add_attendance(self):
        roll_number = input("Enter student's roll number: ")
        student = self.find_student(roll_number)

        if not student:
            print("Student with roll number", roll_number, "not found.")
            return

        date = input("Enter date (YYYY-MM-DD): ")
        status = input("Enter attendance status (Present/Absent): ")
        student.add_attendance(date, status)
        print("Attendance added successfully.")

    def print_student_info(self):
        roll_number = input("Enter student's roll number: ")
        student = self.find_student(roll_number)

        if not student:
            print("Student with roll number", roll_number, "not found.")
            return

        print("Student Information")
        print("Name:", student.name)
        print("Roll Number:", student.roll_number)
        print("Grades:", student.grades)
        print("Average Grade:", student.get_average_grade())
        print("Attendance:", student.attendance)
        print("Attendance Percentage:", student.get_attendance_percentage())


def main():
    sms = StudentManagementSystem()

    while True:
        print("\nStudent Management System")
        print("1. Enroll Student")
        print("2. Add Grade")
        print("3. Add Attendance")
        print("4. Print Student Information")
        print("5. Quit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            sms.enroll_student()
        elif choice == '2':
            sms.add_grade()
        elif choice == '3':
            sms.add_attendance()
        elif choice == '4':
            sms.print_student_info()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == '__main__':
    main()