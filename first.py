print("Hello world! This is my first Python script.")

# Defining variables
x = 5
y=10

# Calculate the sum of variables
sum_result = x + y
print("Sum of numbers", x, "and", y, "equal", sum_result)

# Using the conditional operator
if sum_result > 10:
    print("Sum is greater than 10.")
else:
    print("The amount is not more than 10.")

# Using a for loop to iterate through a list
my_list = [1, 2, 3, 4, 5]
print("List elements:")
for item in my_list:
    print(item)

# Using the function
def multiply(a, b):
    return a * b

# Call a function and output the result
multiply_result = multiply(3, 4)
print("Multiplication result:", multiply_result)
