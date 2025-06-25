import secrets

upper_limit = int(input("Enter the upper limit for the guessing game: "))
random_num = secrets.randbelow(upper_limit + 1)  

while True:
    num_input = int(input("Guess the number: "))
    if num_input == random_num:
        print("Correct!")
        break
    elif num_input > random_num:
        print("Too high!")
    else:
        print("Too low!")