def gradingStudents(grades):
    if grades>=38:
        if grades%5>2:
            return 5*((grades//5)+1)
    return grades
grades_count = int(input().strip())
grades = []

for _ in range(grades_count):
    grades.append(gradingStudents(int(input().strip())))

result = grades
print(result)