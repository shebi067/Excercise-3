


cities = ["Lahore", "Multan", "Karachi", "Quetta", "Peshawar", "Bahawalpur"]
long_cities = []

for city in cities:
    if len(city) > 6:
        long_cities.append(city)

print(long_cities)