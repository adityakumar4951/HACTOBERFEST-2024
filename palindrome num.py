# Function to check if a number is a palindrome
def is_palindrome(num):
    # Convert the number to a string to compare it with its reverse
    num_str = str(num)
    # Check if the string is equal to its reverse
    return num_str == num_str[::-1]

# Input from the user
num = int(input("Enter a number: "))

# Check and display if the number is a palindrome
if is_palindrome(num):
    print(f"{num} is a palindrome number.")
else:
    print(f"{num} is not a palindrome number.")
