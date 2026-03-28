def ceasar_cipher(text, shift):
    encrypted_text = ""
    
    for char in text:
        # Check if the character is a letter(ignores spaces, numbers, punctuation
        if char.isalpha():
            # Determine the base ASCII value: 65 for uppercase 'A', 97 for lowercase 'a'
            base = ord('A') if char.isupper() else ord('a')
            
            # 1. ord(char) - base: Converts the letter to a 0-25 index (e.g., A=0, B=1)
            # 2. + shift: Shifts the letter
            # 3. % 26: Wraps it around if it goes past 'z' (or 25)
            # 4. + base: Converts it back to the correct ASCII range
            new_char = char((ord(char)- base + shift) % 26 + base)
            
            encrypted_text += new_char
        else:
            # If it's not a letter, just add it to the string as-is
            encrypted_text += char
            
    return encrypted_text

# Testing the function
print(ceasar_cipher("abc", 3))
print(ceasar_cipher("xyz", 2))
print(ceasar_cipher("Hello, World!", 5))