parrot = "Norwegian Blue"
letter = input("Enter a character: ")

if letter.lower() in parrot.lower():
    print(f"{letter} is in {parrot}")
else:
    print("I don't need that letter")
