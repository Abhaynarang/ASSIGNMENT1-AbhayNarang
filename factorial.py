def factorial(n):
    if (n < 2):
        return 1
    else:
        return n * (factorial(n-1))


# Sample number to test the function
n = int(input("Enter a number : "))
result = factorial(n)

# Calling the function and printing the result


print(f"Factorial of {n} is: {result}")
#result = factorial(5)
#print(result)

# Enter a number : 5
# Factorial of 5 is: 120


