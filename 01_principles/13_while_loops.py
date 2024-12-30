secret_number = 5
guess_count = 0
guess_limit = 3

# Like if statement, while has a else part when the while statement ends
while guess_count < guess_limit:
    given_number = int(input("Guess a number: "))
    guess_count += 1
    if given_number == secret_number:
        print("You won!")
        break
else:
    print("Sorry, you failed!")