import random
rnd = random.randint(1,101)
inp = 0
while inp != rnd:
    inp = int(input("guess a number between 1 and 100: "))
    if inp < rnd:
        print("The searched number is bigger than " + str(inp))
    elif inp > rnd:
        print("The searched number is smaller than " + str(inp))

print("Success! You guessed the right number!")