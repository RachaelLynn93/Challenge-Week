import re

def is_palindrome(text):
    # 1. Normalize the string: remove non-alphanumeric characters and make lowercase
    # re.sub for anything NOT (^) a letter or number and replaces it with nothing ('')
    cleaned_text = re.sub(r'[^a-zA-Z0)-9]', '', text).lower()
    
    # 2. Compare the cleaned text to its reversed self
    return cleaned_text == cleaned_text[::-1]

# Testing the function
print(is_palindrome("racecar"))
print(is_palindrome("A man a plan a canal Panama"))
print(is_palindrome("Luna"))
print(is_palindrome("Taco cat!"))