
price = [450,1200,300,980,75]

highest = price[0]
lowest = price[0]

for i in price:
     if i > highest:
        highest = i
     if i < lowest:
        lowest = i

print(f"Highest Value: {highest}, Lowest Value: {lowest}")
