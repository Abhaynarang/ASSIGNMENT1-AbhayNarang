
#Problem Statement: Write a Python program that:
#1.  Takes a user's first name and last name as input.
#2.  Concatenates the first name and last name into a full name.
#3.  Prints a personalized greeting message using the full name.

# Step 1: Take the user's first name as input
fname = input("Enter your first name: ")

# Step 2: Take the user's last name as input
lname = input("Enter your last name: ")

# Step 3: Concatenate the first name and last name into a full name
full_name = fname + " " + lname

# Step 4: Print a personalized greeting message
print(f"Hello, {full_name} Welcome to the Python program.")