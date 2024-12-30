def libs_to_kgs(weigth: float):
    return round(weigth * 0.45, 2)

def kgs_to_lbs(weight: float):
    return round(weight / 0.45, 2)

def find_max(numbers):
    max = 0
    for number in numbers:
        if number > max:
            max = number
    return max