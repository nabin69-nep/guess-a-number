import random
number = random.randint(0,100)
guess=int(input("Guess number between 0 and 100:  "))
count=0
while(number!=guess):
    count+=1
    if(count!=1):
     guess=int(input("Guess number between 0 and 100:  "))
    if(guess>number):
     print("Lower number please !")
    elif(guess<number):
     print("Higher number please !")
    else:
     print("Congratulations! You guessed the correct number in",count,"attempts")
