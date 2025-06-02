# Prompt the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize the row counter
row = 0

# Use a while loop to iterate through rows
while row < size:
    # For each row, print 'size' asterisks side by side
    for _ in range(size):
        print("*", end="")
    # Move to the next line after printing one row
    print()
    # Increment the row counter
    row += 1

