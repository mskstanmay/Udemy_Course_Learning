answer = 50

print("Please guess a number between 1 and 100: ")
guess = int(input())

if guess != answer:
    if guess < answer:
        print("Guess higher.")
    else:
        print("Guess lower.")
    guess = int(input())
    if guess == answer:
        print("Well Done.")
    else:
        print("Wrong......")
else:
    print("You got it first time !")

# if guess < answer:
#     print("Please guess higher")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, You got it right.")
#     else:
#         print("Incorrect Guess")
# elif guess > answer:
#     print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, You got it right.")
#     else:
#         print("Incorrect Guess")
# else:
#     print("You got it first time")
