

numbers = [12, 7, 9, 20, 33, 48, 51]
result = {"even": 0, "odd": 0}

for i in numbers:
    if i%2 == 0:
        result["even"]+=1
    else:
        result["odd"]+=1

print(result)