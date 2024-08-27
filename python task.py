from math import sqrt

# Function to check if a string is a palindrome and count character frequencies
def is_palindrome(s):
    # Remove spaces and convert to lowercase for consistent comparison
    s = s.replace(" ", "").lower()
    # Check if the string reads the same forwards and backwards
    is_palind = s == s[::-1]
    # Count the frequency of each character
    freq_dict = {}
    for char in s:
        freq_dict[char] = freq_dict.get(char, 0) + 1
    return (is_palind, freq_dict)

# Function to check if a number is a prime number and list divisors
def is_prime(n):
    if n <= 1:
        return []
    if n == 2:
        return [(False, 2)]
    
    divisors = [(n % i == 0, i) for i in range(2, int(sqrt(n)) + 1)]
    return divisors

# Main program
def main():
    results = []
    failed_attempts = []

    for _ in range(3):  # Allow up to 3 retries
        try:
            # User input for palindrome check
            user_string = input("Enter a string to check for palindrome: ")
            palindrome_result = is_palindrome(user_string)
            is_palind = palindrome_result[0]
            char_frequencies = palindrome_result[1]

            # User input for prime number check
            user_number = int(input("Enter a number to check if it's prime: "))
            prime_result = is_prime(user_number)
            
            # Store results
            result = {
                "input_string": user_string,
                "palindrome_check": {
                    "is_palindrome": is_palind,
                    "character_frequencies": char_frequencies
                },
                "prime_check": prime_result
            }
            results.append(result)
            break  # Exit loop if inputs are valid
        except ValueError as ve:
            # Log failed attempt
            failed_attempts.append((input, str(ve)))
            print(f"Invalid input. Error: {ve}. Please try again.")
    
    # Print the results
    print("Results:")
    for res in results:
        print(res)
    
    # Print failed attempts if any
    if failed_attempts:
        print("\nFailed attempts:")
        for failed in failed_attempts:
            print(f"Input: {failed[0]}, Error: {failed[1]}")

if __name__ == "__main__":
    main()