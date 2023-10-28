if {} or 0 or "":
    print("True")
else:
    print("False")

name = input('Please enter your name: ')
#if name:
if name != "":
    print(f"Hello, {name}")
else:
    print("Mr. Nameless pleasure to meet you.")
