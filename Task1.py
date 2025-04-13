#Problem Statement: Write a Python program that does the following:
#1.  Takes two numbers as input from the user.
#2.  Performs the basic mathematical operations on these two numbers:
#	Addition
#	Subtraction
#	Multiplication
#	Division.

#3.  Displays the results of each operation on the screen.

 #Expected Output:
#The output should include the result of each operation performed.

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

# Perform the addition
addition = a + b

#Subtraction
subtraction = a - b

# Multiplication
multiplication = a * b

#Division
division = a / b

# Display the result
print(f"Addition: {a} + {b} = {addition}")

print(f"Subtraction: {a} - {b} = {subtraction}")

print(f"Multiplication: {a} * {b} = {multiplication}")

print(f"Division: {a} / {b} = {division}")
