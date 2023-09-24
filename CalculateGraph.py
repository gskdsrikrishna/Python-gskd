def calculate_grade(assignments, exams, weights):
    assignment_grade = sum(assignments) / len(assignments)
    exam_grade = sum(exams) / len(exams)
    
    assignment_weight = weights[0]
    exam_weight = weights[1]
    
    total_grade = (assignment_grade * assignment_weight) + (exam_grade * exam_weight)
    return total_grade

def main():
    num_assignments = int(input("Enter the number of assignments: "))
    assignments = []
    for i in range(num_assignments):
        grade = float(input(f"Enter the grade for assignment {i+1}: "))
        assignments.append(grade)
    
    num_exams = int(input("Enter the number of exams: "))
    exams = []
    for i in range(num_exams):
        grade = float(input(f"Enter the grade for exam {i+1}: "))
        exams.append(grade)
    
    assignment_weight = float(input("Enter the weight for assignments (between 0 and 1): "))
    exam_weight = float(input("Enter the weight for exams (between 0 and 1): "))
    
    weights = [assignment_weight, exam_weight]
    
    grade = calculate_grade(assignments, exams, weights)
    print("Final grade:", grade)

if __name__ == "__main__":
    main()\