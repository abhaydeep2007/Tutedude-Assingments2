# Task 1: Check if a Number is Even or Odd

# 1. Takes an integer input from the user [cite: 6]
number = int(input("Enter a number: "))

# 2. Checks whether the number is even or odd using an if-else statement [cite: 8]
if number % 2 == 0:
    # 3. Displays the result accordingly [cite: 10]
    print(f"{number} is an even number.")
else:
    print(f"{number} is an odd number.")
