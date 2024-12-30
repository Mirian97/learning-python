try:
    age = int(input("Age: "))
    income = 2000
    risks = 2000 / age
except ValueError:
    print("Invalid number")
except ZeroDivisionError:
    print("0 is not valid value")
