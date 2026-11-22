students = [
    {"name": "Ali", "marks": [80, 75, 90]},
    {"name": "Sara", "marks": [95, 88, 92]},
    {"name": "Ahmed", "marks": [55, 62, 48]},
]

highest_average = 0
tooper = ""

for i in students:
    name = i["name"]
    marks = i["marks"]
   
    total = 0
    count = 0
    for mark in marks:
        total += mark
        count += 1

    average = total / count

    result = "Pass" if average > 60 else "Fail"
    print(f"{name}, {average} {result}")

    if average >  highest_average:
        highest_average = average
        tooper = name


print(f"Topper: {tooper}")


 

