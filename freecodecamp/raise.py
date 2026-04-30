# the raise statement is a powerful tool that allows you to manually trigger exceptions in your code

# It gives you control over when and how errors are generated, enabling you to create custom error conditions 
# and enforce specific program behavior

# The raise statement is used to explicitly throw an exception at any point in your program, 
# allowing you to signal that an error condition has occurred or that certain requirements haven't been met.

def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age

try:
    check_age(-5)
except ValueError as e:
    print(f"Error: {e}")

# In this example, we're raising a ValueError with a custom message when an invalid age is provided

def process_data(data):
    try:
        result = int(data)
        return result * 2
    except ValueError:
        print("Logging: Invalid data received")
        raise

try:
    process_data('abc')
except ValueError:
    print('Handled at higher level')

class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f'Insufficient funds ${balance} available, ${amount} requested')

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    return balance - amount

try:
    new_balance = withdraw(100, 150)
except InsufficientFundsError as e:
    print(f"Transaction failed: {e}")

def parse_config(filename):
    try:
        with open(filename, 'r') as file:
            data = file.read()
            return int(data)
    except FileNotFoundError:
        raise ValueError("Configuration file is missing") from None
    except ValueError as e:
        raise ValueError("Invalid configuration format") from e
    

config = parse_config("config.txt")

def calculate_square_root(number):
    assert number >= 0, 'Cannot calculate square root of negative number'
    return number ** 0.5

try:
    result = calculate_square_root(-4)
except AssertionError as e:
    print(f"Assertation failed: {e}")

