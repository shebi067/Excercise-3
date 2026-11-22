


marks = [78,45,92,33,67,68]
passed_count= 0
for i in marks:
    if i >= 40:
        print(f"{i}, Pass")
        passed_count+=1
    else:
        print("Fail")

print(f"Passed: ", {passed_count})