# ASSINGMENT 3
#randomly guess a number
import random
print("you have 20 chances")
user = int(input("enter a number between 1,200: "))
guess = random.randint(1,200)
for i in range(20):
  if user==guess:
    print("you guessed right")
    break
  elif user>guess:
    print("your guess is higher")
    user = int(input("try again enter another number: "))
    continue
  elif user<guess:
    print("your guess is lower")
    user = int(input("try again enter another number: "))
    continue
  else:
    print("your number is not realistic")
else:
  print("you runned out of chances")
