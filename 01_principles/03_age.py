from datetime import datetime

birth_year = input("Birth year: ")
age = datetime.now().year - int(birth_year)
print("You are " + str(age) + " years old.")

# To check the type
print(type(birth_year))
print(type(age))