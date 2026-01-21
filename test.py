name = input("Enter your name: ")
age = int(input("Enter your age: "))

print(f"Hello, {name}! You are {age} years old.")
if age < 18:
    print("You are a minor.")
else:
    print("You are an adult.")