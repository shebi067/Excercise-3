

students = {"Ali": 85, "Sara": 92, "Ahmed": 76, "Hina": 58, "Bilal": 64}
student_name = []
total_number = 0

for name, number in students.items() :
    total_number += number
    if number>80:
        grade = "A"
    elif number>70:
        grade = "B"
    elif number > 60:
        grade = "C"
    else:
        grade = "f"

    student_name.append(f"{name}, {grade}")


average = total_number / len(students)
print(average)

print(f"{student_name}" )