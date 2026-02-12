'''
5. Write a function inside another function.
'''
def outer_function(x, y):
    # Inner function defined inside outer_function
    def inner_addition(a, b):
        return a + b
    
    # Using the inner function
    result = inner_addition(x, y)
    return result * 2  # Outer function does something extra


# Example usage
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Final result:", outer_function(num1, num2))
