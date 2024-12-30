weigth = float(input("Weight: "))
unit = input("(L)bs or (K)g: ")

if unit.upper() == "L":
    converted = round((weigth * 0.45), 2)
    print(f"You are {converted} kilos.")
elif unit.upper() == "K":
    converted = round((weigth / 0.45), 2)
    print(f"You are {converted} pounds.")
else:
    print("Choose between L ou K.")