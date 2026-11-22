
nums = [3, 5, 3, 8, 5, 3, 9]

counts = {}
for num in nums:
    if num in counts:
        counts[num] += 1
    else:
        counts[num] = 1

unique_nums = list(counts.keys())

most_frequent_num = None
max_count = 0

for num, freq in counts.items():
    if freq > max_count:
        max_count = freq
        most_frequent_num = num

print(f"unique {unique_nums} most frequent {most_frequent_num} ({max_count} times)")