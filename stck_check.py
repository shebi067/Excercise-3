
products = [    ("Laptop", 150000, 3), ("Mouse", 2500, 0),
("Keyboard", 5000, 12), ("Monitor", 45000, 2)]
out_of_stock= []
low_stock= []
total = 0
for name, price, quantity in products:
    total += price*quantity
    if quantity == 0:
        out_of_stock.append(name)
    elif quantity <=5:
        low_stock.append(name)


print(f"low stock, {','.join(low_stock)}")
print(f"Out of Stock, {','.join(out_of_stock)}")

print(total)

    
    


