# for i in range (1,11):
#     print(f"Number: {i:2} | Square: {i**2:3} | Cube: {i**3:4} ")
# print("_" * 40)

# Vote system - If else
name = input("Enter your name: ")
age = int(input("Age: "))
print(age)

if (age >= 18):
    print("Congratulations You can vote !")
    print("Please put an X in the box")
elif age == 99:
    print("One final vote that marks the end")
else:
    print(f"Sorry But you need to wait {18-age} years to vote.")
