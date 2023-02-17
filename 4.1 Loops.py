import random

seedVal = int(input("What seed should be used? "))
random.seed(seedVal)

print("What is the upper bound?")
upper = int(input())
print("What is the lower bound?")
while 1:
    lower = int(input())
    if lower < upper:
        lower == lower
        break
    else:
        print("What is the lower bound?")

answer = int(random.randint(lower, upper))
#print(answer)
print("What is your guess?")
while 1:
    guess = int(input())
    if guess < answer:
        print("Nope, too low.")
    elif guess > answer:
        print("Nope, too high.")
    elif guess == answer:
        print("You got it!")
        exit(1)