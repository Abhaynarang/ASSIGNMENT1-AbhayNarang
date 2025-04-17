import math  # Importing the math module

# Step 1: Ask the user for a number as input
num = float(input("Enter a number: "))

# Step 2: Perform mathematical calculations
square_root = math.sqrt(num)  # Calculate the square root
natural_log = math.log(num)   # Calculate natural logarithm (log base e)
sine_value = math.sin(num)    # Calculate sine of the number in radians

# Step 3: Display the results
print(f"Square root : {square_root}")
print(f"Logarithm : {natural_log}")
print(f"Sine : {sine_value}")

##Enter a number: 25
##Square root : 5.0
##Logarithm : 3.2188758248682006
##Sine : -0.13235175009777303
