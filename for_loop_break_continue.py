# Guided Coding Exercise: for Loop with break and continue

# Create a list of numbers from 1 to 10
numbers = list(range(1, 11))

# Iterate over each number in the list
for num in numbers:
    # Skip the number 3
    if num == 3:
        continue  # Skip this iteration and move to the next number
    
    # Stop the loop when the number is 7
    if num == 7:
        break  # Exit the loop completely

    # Print the current number
    print(num)