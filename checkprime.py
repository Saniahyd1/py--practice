def is_prime(num):
    # Numbers less than or equal to 1 are not prime
    if num <= 1:
        return False
    
    # 2 is the only even prime number
    if num == 2:
        return True
        
    # Exclude all other even numbers
    if num % 2 == 0:
        return False

    # Check odd factors up to the square root of the number
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False  # Found a factor, so it's not prime
            
    return True  # No factors found, it is prime

# --- Take input from the user ---
try:
    user_input = int(input("Enter an integer to check: "))
    
    if is_prime(user_input):
        print(f"{user_input} is a prime number.")
    else:
        print(f"{user_input} is NOT a prime number.")
except ValueError:
    print("Please enter a valid integer.")
