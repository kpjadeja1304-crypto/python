'''
3. WAP 1 2 +2 2 +3 2 +………………….n 2
'''
n = int(input("Enter n: "))
total = sum(i**2 for i in range(1, n+1))
print("Sum of squares =", total)
