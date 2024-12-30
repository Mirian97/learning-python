digit_mapping = {
    "0": "Zero",
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine" 
}

phone = input("Phone: ")
formatted_phone = ""

for digit in phone:
    digit_founded = digit_mapping.get(digit, "!")
    formatted_phone += f"{digit_founded} "

print(formatted_phone)