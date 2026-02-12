'''
6. Banking System Using Functions
   Functions for:
   Deposit
   Withdraw
   Check Balance
'''
# Global variable to store balance
balance = 0

def deposit(amount):
    global balance
    if amount > 0:
        balance += amount
        return f"Deposited {amount}. Current balance: {balance}"
    else:
        return "Deposit amount must be positive."

def withdraw(amount):
    global balance
    if amount > balance:
        return "Insufficient funds!"
    elif amount <= 0:
        return "Withdrawal amount must be positive."
    else:
        balance -= amount
        return f"Withdrew {amount}. Current balance: {balance}"

def check_balance():
    return f"Current balance: {balance}"


# Example usage
while True:
    print("\nBanking System Menu:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Enter choice (1/2/3/4): ")

    if choice == '1':
        amt = float(input("Enter amount to deposit: "))
        print(deposit(amt))
    elif choice == '2':
        amt = float(input("Enter amount to withdraw: "))
        print(withdraw(amt))
    elif choice == '3':
        print(check_balance())
    elif choice == '4':
        print("Exiting... Thank you for banking with us!")
        break
    else:
        print("Invalid choice. Please try again.")
