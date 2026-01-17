# Task 2: Sum of Integers from 1 to 50 Using a Loop

total_sum = 0

# 1. Uses a for loop to iterate over numbers from 1 to 50 [cite: 19]
# Note: range(1, 51) goes from 1 up to, but not including, 51
for i in range(1, 51):
    # 2. Calculates the sum of all integers in this range [cite: 20]
    total_sum += i

# 3. Displays the final sum [cite: 21]
# Expected Output: "The sum of numbers from 1 to 50 is: 1275" [cite: 25]
print(f"The sum of numbers from 1 to 50 is: {total_sum}")
