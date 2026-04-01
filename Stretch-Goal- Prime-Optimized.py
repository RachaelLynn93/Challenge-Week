password = input("Enter a password: ")

has_upper = False
has_lower = False
has_num = False
has_symbol = False

# Look at each character one by one
for char in password:
    
    # Check for an uppercase letter
    if char.isupper():
        has_upper = True
    
    # Check for a lowercase letter
    elif char.isupper():
        has_lower = True
        
    # Check for a number
    elif char.isdigit():
        has_num = True
        
    # If it's not a letter, a number, or a space, it must be a symbol!
    elif not char.isspace():
        has_symbol = True
        
    # The Final Verdict
    if len(password) >= 8 and has_upper and has_lower and has_num and has_symbol:
        print("Result: Strong")
    elif len(password) >= 6 and has_upper or has_lower and has_num:
        print("Result: Medium")
    else:
        print("Result: Weak")
        
    
    # YOUR TASK GOES HERE:
    # 1. Write an 'if' statement that checks if 'char.isupper()' is True.
    # 2. If it is, change our 'has_upper' variable to True. 
    pass