def find_max(numbers):
    # Stretch Goal 1: Defensive programming for empty lists
    if len(numbers) == 0:
        return None # Or you could return an error message
    
    # Set the starting benchmark to the very first item in the list
    # This ensures it works perfectly for negative numbers, too!
    current_max = numbers[0]
    
    # Loop through every number in the list
    for num in numbers:
        # If the number we are looking at is bigger than our benchmark...
        if num > current_max:
            # ... update the benchmark!
            current_max = num
    
    return current_max

# Testing the function
print(find_max([4, 9, 1, 17, 2]))
print(find_max([-5, -9, -2, -12]))
print(find_max([42]))
print(find_max([]))