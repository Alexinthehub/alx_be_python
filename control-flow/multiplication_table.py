# Ask the user to input a number
number = int(input("Enter a number to see its multiplication table: "))

# Loop from 1 to 10 to generate the multiplication table
for i in range(1, 11):
    product = number * i
    print(f"{number} * {i} = {product}")

