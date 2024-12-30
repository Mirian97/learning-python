has_good_credit = False
price_of_house = 1000000
discount = 0

if has_good_credit:
    discount = 0.1
else:
    discount = 0.2

down_payment = round(discount * price_of_house)
    
print(f"Discount of price is: {down_payment}")