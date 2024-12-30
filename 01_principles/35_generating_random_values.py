import random

for i in range(3):
    print(random.random())

for i in range(3):
    print(random.randint(10, 25))
    
members = ["Mirian", "Evair", "Iago", "Hamed"]
print(random.choice(members))