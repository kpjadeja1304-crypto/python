'''
5. Write a function inside another function.
'''

def cal(x, y):
    # Inner function defined inside outer_function
    def add():
        return x + y
    
    def multi():
        return x * y
    
    # Returning results of inner functions
    return add(), multi()

# Example usage
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

addition, multiplication = cal(num1, num2)

print("Addition result:", addition)
print("Multiplication result:", multiplication)
