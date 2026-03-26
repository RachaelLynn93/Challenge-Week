def is_prime(n):
    # Hint 1: Any number less than 2 is not prime(this handles 0, 1, and negative numbers)
    if n < 2: 
        return False
    
    # Hint 3: Loop from 2 up to n-1
    for i in range(2, n):
        # Hint 2: Use % to check for divisibility
        # If n is evenly divisible by i, it has a divisor other than 1 and itself
        if n % i == 0:
            return False # We found a divisor, so it's definitively NOT prime
        
        # If the loop finishes entirely and never triggered the 'return False', 
        # then the number must be prime
        return True
    
# Testing the Function
print(is_prime(2))
print(is_prime(11))
print(is_prime(15))
print(is_prime(1))
print(is_prime(0))