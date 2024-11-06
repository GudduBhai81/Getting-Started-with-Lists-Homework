# Get the range from the user
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

# Create a list of squares of numbers in the specified range
squares = [num ** 2 for num in range(start, end + 1)]

# Separate the squares into odd and even lists
odd_squares = [square for square in squares if square % 2 != 0]
even_squares = [square for square in squares if square % 2 == 0]

# Display the results
print("List of squares:", squares)
print("List of odd squares:", odd_squares)
print("List of even squares:", even_squares)
