def find_max_with_index(numbers):
    if not numbers:
        return None, None
    
    current_max = numbers[0]
    max_index = 0
    
    # Loop through the indices of the list instead of the items directly
    for i in range(len(numbers)):
        if numbers[i] > current_max:
            current_max = numbers[i]
            max_index = i # Save the position where we found the new max
            
    return current_max, max_index

print(find_max_with_index([4, 9, 1, 17, 2]))