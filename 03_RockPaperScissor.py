import random

user_wins = 0 
computer_wins = 0
user_name = input("Enter Your Name: ")
print(f"Welcome {user_name}")

options = ['rock','paper','scissor']

while True:
    user_input = input("Type Rock/Paper/Scissor or q to quit: ").lower()
    if user_input.lower().strip() == "q":
        break
    if user_input not in options:
        continue
    
    random_number = random.randint(0,2)
    computer_picks = options[random_number]
    print("Computer Picked: ",computer_picks)
    
    if user_input == 'rock' and computer_picks == 'scissor':
        print("User Won")
        user_wins+=1
    elif user_input =='paper' and computer_picks == 'rock':
        print("User Won")    
        user_wins+=1
    elif user_input == 'scissor' and computer_picks == 'scissor':
        print("User Won")    
        user_wins+=1
    elif user_input == computer_picks:
        print("Tie")
        continue
    else:
        print("User Lost")
        computer_wins+=1    
        
print(f"{user_name} won {user_wins} times")
print(f"Computer won {computer_wins} times")
print("Good Bye")
    
    