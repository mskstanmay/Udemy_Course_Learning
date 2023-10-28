age = float(input("Enter your age: "))
name = input("Enter your name: ")

if age and name:
    if 18 <= age < 31:
        print("Welcome aboard {}".format((name)))
    else:
        print("No...")
