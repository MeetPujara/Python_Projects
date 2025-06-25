print("Welcome to Quiz")

playing = input("Do u want to play? ")

if playing.lower().strip() != "yes":
    quit()

print("Okay Lets Play :)")
score = 0

answer = input("What does full form of CPU? ")

if answer.lower().strip() == "central processing unit":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")
    
    
answer = input("What does full form of RAM? ")
if answer.lower().strip() == "random access memory":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")
    
    
answer = input("What does full form of GPU? ")
if answer.lower().strip() == "graphics processing unit":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")
    
    
answer = input("What does full form of ROM? ")
if answer.lower().strip() == "read only memory":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")
    
    
answer = input("What does full form of PSU? ")
if answer.lower().strip() == "power supply unit":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

print(f"Your got {score} questions correct")