numbers = [22, 23, 23, 45, 40, 45, 35]
unique_numbers = []

for number in numbers:
    if(number not in unique_numbers):
        unique_numbers.append(number)

print(unique_numbers)