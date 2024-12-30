numbers = [2, 5, 6, 12, 9, 45]

numbers2 = numbers.copy()
numbers.append(20)
print(numbers2)

# Display Error if index not found
# print(numbers.index(4))

numbers.insert(6, 23)
numbers.sort()
numbers.remove(12)
numbers.reverse()
numbers.pop()
numbers.pop()
print(numbers)
print(45 in numbers)
print(100 in numbers)