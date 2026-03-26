def reverse_string_loop(text):
    reversed_text = "" # Create an empty string to hold our result
    
    for char in text:
        # Prepend the current character to the front of our reversed string
        reversed_text = char + reversed_text
        
    return reversed_text

# Testing the function 
print(reverse_string_loop("hello"))
print(reverse_string_loop("Python"))
