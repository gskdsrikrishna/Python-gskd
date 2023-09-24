class Student:
    def __init__(self, student_id, name, grade):
        self.student_id = student_id
        self.name = name
        self.grade = grade
        self.courses = []

    def add_course(self, course):
        self.courses.append(course)

    def display_courses(self):
        if not self.courses:
            print("No courses registered.")
        else:
            print("Registered courses:")
            for course in self.courses:
                print(course)


class Course:
    def __init__(self, course_id, name):
        self.course_id = course_id
        self.name = name


class StudentInformationSystem:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def find_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None


# Creating the Student Information System instance
sis = StudentInformationSystem()

# Creating students and courses
student1 = Student(1, "John Smith", "10th Grade")
student2 = Student(2, "Jane Doe", "11th Grade")

course1 = Course(101, "Mathematics")
course2 = Course(102, "Science")

# Adding courses for students
student1.add_course(course1)
student2.add_course(course1)
student2.add_course(course2)

# Adding students to the Student Information System
sis.add_student(student1)
sis.add_student(student2)

# Searching for a student and displaying their courses
searched_student_id = 2
searched_student = sis.find_student(searched_student_id)

if searched_student:
    print("Student found:")
    print("Student ID:", searched_student.student_id)
    print("Name:", searched_student.name)
    print("Grade:", searched_student.grade)
    searched_student.display_courses()
else:
    print("Student not found.")